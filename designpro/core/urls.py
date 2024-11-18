from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='core:home'),
    path('create-request/', views.create_request, name='core:create_request'),
    path('view-requests/', views.view_requests, name='core:view_requests'),
    path('delete-request/<int:pk>/', views.delete_request, name='core:delete_request'),
    path('change-request-status/<int:pk>/', views.change_request_status, name='core:change_request_status'),
    path('admin-panel/', views.admin_panel, name='core:admin_panel'),
    path('add-category/', views.add_category, name='core:add_category'),
    path('delete-category/<int:pk>/', views.delete_category, name='core:delete_category'),
]
