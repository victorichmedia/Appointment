from django.urls import path
from . import views
from .views import registration_view



urlpatterns = [
    path('myappointments/', views.AppointmentBookByClientListView.as_view(), name='my-appointment'),

    path('register/', registration_view, name='register'),

]
