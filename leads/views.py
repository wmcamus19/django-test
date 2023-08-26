from typing import Any, Dict
from django.db import models
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from leads.models import Lead

# Create your views here.


class LeadListView(ListView):
    # dev: path('', LeadListView.as_view(), name='lead_list'),
    model = Lead
    template_name = "leads/lead_list.html"
    paginate_by = 50
    context_object_name = 'leads'

    # dev: This is also acceptable
    # queryset = Lead.objects.filter(first_name__startswith='D').values()

    def get_queryset(self):
        queryset = super(LeadListView, self).get_queryset()
        # dev: I need the .values to convert it into dictionary insted of instance.
        queryset = queryset.filter(first_name__startswith='E').values()
        return queryset

    # dev: For data manipulation before sending it to the template view.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # dev: Adding additional variables with values.
        context.update({
            'tab_title': 'Leads Page',
            'webpage_title': 'Leads Page!!',
            'my_string': 'original value',
        })
        return context


class LeadDetailView(DetailView):
    # dev: path('<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),
    model = Lead
    template_name = "leads/lead_detail.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)


class LeadCreateView(CreateView):
    # dev: path('create/', LeadCreateView.as_view(), name='lead_create'),
    model = Lead
    fields = ["first_name", "last_name", "age", "agent",]
    template_name = "leads/lead_create.html"
    success_url = reverse_lazy("leads:lead_create")


class LeadUpdateView(UpdateView):
    # dev: path('edit/<int:pk>/', LeadUpdateView.as_view(), name='lead_update'),
    model = Lead
    fields = ["first_name", "last_name", "age", "agent",]
    template_name_suffix = "_update_form"

    # # dev: pre-method.
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset

    # dev: pre-method. depended to get_queryset method.
    def get_object(self, queryset: models.QuerySet[Any] = None) -> models.Model:
        obj = super().get_object(queryset)

        # dev: I changed the two values before sending it to the get_context_data method.
        obj.last_name = 'awd'
        obj.age = 102
        return obj

    # dev: pre-method. depended to get_object method.
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)

    # dev: post-method.
    def get_success_url(self) -> str:
        if self.object.pk:
            # dev: I use this for navigation on lead_detail url to provide the pk instead of 'success_url' attribute.
            return reverse_lazy('leads:lead_detail', kwargs={'pk': self.object.pk})
        else:
            return super().get_success_url()


class LeadDeleteView(DeleteView):
    # dev: path('delete/<int:pk>/', LeadDeleteView.as_view(), name='lead_delete'),
    model = Lead
    template_name_suffix = "_confirm_delete"
    # dev: reverse_lazy is good for returning to the path. and it does have args and kwargs to passed.
    success_url = reverse_lazy('leads:lead_list')
