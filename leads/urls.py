from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
# TODO. for referencing the namespace='leads' on the root urls.py

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='lead_list'),
    path('create/', login_required(LeadCreateView.as_view()), name='lead_create'),
    path('test/', HomePageView.as_view(), name='test'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),
    # path('create/', login_required(LeadCreateView.as_view(template_name="leads/lead_create.html")), name='lead_create'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead_delete'),
    path('<int:pk>/edit/', LeadUpdateView.as_view(), name='lead_update'),
]
