from django.urls import path
from . import views


urlpatterns = [
    path('appointments/', views.CreateAppointmentListView.as_view(), name='appointment_list'),
    path('appointment/<int:pk>', views.CreateAppointmentDetailView.as_view(), name='appointment_detail'),

    path('appointment/create/', views.CreateAppointmentCreate.as_view(), name='appointment-create'),
    path('appointment/<int:pk>/update/', views.CreateAppointmentUpdate.as_view(), name='appointment-update'),
    path('appointment/<int:pk>/delete/', views.CreateAppointmentDelete.as_view(), name='appointment-delete'),
]