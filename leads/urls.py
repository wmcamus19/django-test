from django.urls import path
from .views import *

# TODO. for referencing the namespace='leads' on the root urls.py
app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='lead_list'),
    path('test/', HomePageView.as_view(), name='test'),
    path('create/', LeadCreateView.as_view(), name='lead_create'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead_delete'),
    path('<int:pk>/edit/', LeadUpdateView.as_view(), name='lead_update'),
]
