import typing
from typing import Any
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.db import models
from django.db.models.query import QuerySet
from django.forms.forms import BaseForm
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)


from .models import Lead, User

# Create your views here.


class TestView (CreateView):

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        student_number = f"SN"
        form.instance.student_number = student_number
        return super().form_valid(form)


class HomePageView(ListView):
    model = User
    template_name = "leads/home.html"
    context_object_name = 'users'

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super(HomePageView, self).get_queryset()
        return queryset


class CustomLoginView(LoginView):
    template_name = './registration/login.html'

    def get_form(self, form_class: type[AuthenticationForm] = None) -> BaseForm:
        form = super().get_form(form_class)
        form.fields['username'].widget.attrs.update(
            {'class': 'custom-class wtf', 'disabled': False,
             'aria-label': 'Haha', 'placeholder': 'NANDATO!?', 'value': 'Not true', 'id': 'adasd'})
        form.fields['username'].help_text = 'sauce everyone?'
        form.fields['password'].help_text = 'Not interested.'

        return form

    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        # Intentionally add an error to the username field
        # form.add_error(
        #     'username', 'This is an intentional error for the username field.')
        # form.add_error(
        #     'password', 'This is an intentional error for the password field.')
        return super().form_invalid(form)


class LeadListView(ListView):
    # TODO: path('', LeadListView.as_view(), name='lead_list'),
    model = Lead
    template_name = "leads/lead_list.html"
    paginate_by = 50
    context_object_name = 'leads'

    # TODO: This is also acceptable
    # queryset = Lead.objects.filter(first_name__startswith='D').values()

    def get_queryset(self):
        queryset = super(LeadListView, self).get_queryset()
        # TODO: I need the .values to convert it into dictionary insted of instance.
        queryset = queryset.filter(first_name__startswith='E').values()
        return queryset

    # TODO: For data manipulation before sending it to the template view.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: Adding additional variables with values.
        context.update({
            'tab_title': 'Leads Page',
            'webpage_title': 'Leads Page!!',
            'aw': 'original value',
        })
        return context


class LeadDetailView(DetailView):
    # TODO: path('<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),
    model = Lead
    template_name = "leads/lead_detail.html"

    def get_context_data(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        return super().get_context_data(**kwargs)


@method_decorator(login_required, name='dispatch')
class LeadCreateView(LoginRequiredMixin, CreateView):
    # TODO: path('create/', LeadCreateView.as_view(), name='lead_create'),
    model = Lead
    fields = ["first_name", "last_name", "age", "agent",]
    template_name = "leads/lead_create.html"
    success_url = reverse_lazy('leads:lead_create')
    # def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
    #     if not request.user.is_authenticated:
    #         return reverse_lazy('leads:leads_list')

    #     return super().get(request, *args, **kwargs)

    def get_form(self, form_class: type[BaseModelForm] = None) -> BaseModelForm:
        form = super().get_form(form_class)
        form.fields["first_name"].widget.attrs.update(
            {"placeholder": "Nani", })
        form.fields["age"].widget.attrs.update({"min": 0, "max": 10, })

        return form

    # TODO: Form validation before sending the email.

    def form_valid(self, form: BaseModelForm) -> HttpResponse:

        # TODO: Credential is for testing purposes.
        send_mail(subject='Cool Subject.', message='This is a cool subjects',
                  from_email='test@test.com', recipient_list=['test2@test.com'],)
        return super().form_valid(form)


class LeadUpdateView(UpdateView):
    # TODO: path('edit/<int:pk>/', LeadUpdateView.as_view(), name='lead_update'),
    model = Lead
    fields = ["first_name", "last_name", "age", "agent",]
    template_name_suffix = "_update_form"

    def get_form(self, form_class: type[BaseModelForm] = None) -> BaseModelForm:
        form = super().get_form(form_class)
        form.fields['age'].widget.attrs.update({'min': 0, 'max': 10})

        return form

    # # TODO: pre-method.
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset

    # TODO: pre-method. depended to get_queryset method.
    def get_object(self, queryset: models.QuerySet[typing.Any] = None) -> models.Model:
        obj = super().get_object(queryset)

        # TODO: I changed the two values before sending it to the get_context_data method.
        obj.last_name = 'awd'
        obj.age = 102
        return obj

    # TODO: pre-method. depended to get_object method.
    def get_context_data(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        return super().get_context_data(**kwargs)

    # TODO: post-method.
    def get_success_url(self) -> str:
        if self.object.pk:
            # TODO: I use this for navigation on lead_detail url to provide the pk instead of 'success_url' attribute.
            return reverse_lazy('leads:lead_detail', kwargs={'pk': self.object.pk})
        else:
            return super().get_success_url()


class LeadDeleteView(DeleteView):
    # TODO: path('delete/<int:pk>/', LeadDeleteView.as_view(), name='lead_delete'),
    model = Lead
    template_name_suffix = "_confirm_delete"
    # TODO: reverse_lazy is good for returning to the path. and it does have args and kwargs to passed.
    success_url = reverse_lazy('leads:lead_list')
