from django.urls import path
from . import views


urlpatterns = [
    path('myappointments/', views.AppointmentBookByClientListView.as_view(), name='my-appointment'),

    path('user/', views.UserListView.as_view(), name="user-list"),
    path('user/<int:pk>', views.UserDetailView.as_view(), name="user-detail"),

    path('doctors/', views.DoctorListView.as_view(), name="doctor-list"),
    path('doctor/<int:pk>', views.DoctorDetailView.as_view(), name="doctor-detail"),

    path('user/create/', views.UserCreate.as_view(), name='user-create'),
    path('user/<int:pk>/update/', views.UserUpdate.as_view(), name='user-update'),
    path('user/<int:pk>/delete/', views.UserDelete.as_view(), name='user-delete'),

    path('doctor/create/', views.DoctorCreate.as_view(), name='doctor-create'),
    path('doctor/<int:pk>/update/', views.DoctorUpdate.as_view(), name='doctor-update'),
    path('doctor/<int:pk>/delete/', views.DoctorDelete.as_view(), name='doctor-delete'),
]
