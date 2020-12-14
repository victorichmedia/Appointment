from django.shortcuts import render
from .models import CreateAppointment
from django.views import generic
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CreateAppointmentListView(generic.ListView):
    model = CreateAppointment
    context_object_name = 'appointment_list'   # your own name for the list as a template variable
    queryset = CreateAppointment.objects.all() # Get All Appointment
    template_name = 'record/record_list.html'  # Specify your own template name/location
    paginate_by = 10

class CreateAppointmentDetailView(generic.DetailView):
    model = CreateAppointment


class CreateAppointmentCreate(LoginRequiredMixin,CreateView):
    model = CreateAppointment
    fields = '__all__'

class CreateAppointmentUpdate(UpdateView):
    model = CreateAppointment
    fields = '__all__'

class CreateAppointmentDelete(DeleteView):
    model = CreateAppointment
    fields = '__all__'