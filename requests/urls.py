from django.urls import path
from .views import *

urlpatterns = [
    path('create-request/', RequestView.as_view(), name='create-request'),
    path('', EmployeeRequestsView.as_view(), name='employee-my-requests'),
    path('<slug:slug>/', RequestSingleView.as_view(), name='request_single'),
    path('manager/<slug:slug>/', ManagerSingleView.as_view(), name='request_super_user_single'),
    
]