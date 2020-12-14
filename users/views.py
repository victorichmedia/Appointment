from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from record.models import AppointmentInstance
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.urls import reverse

from .models import Doctor, User

# Create your views here.

class AppointmentBookByClientListView(LoginRequiredMixin,generic.ListView):
    model = AppointmentInstance
    template_name ='appointment/appointment_book_by_client.html'
    paginate_by = 10
    
    def get_queryset(self):
        return AppointmentInstance.objects.filter(client=self.request.user).filter(status__exact = 'Pending')

class DoctorListView(generic.ListView):
    model = Doctor
    context_object_name = 'doctor_list' 
    template_name ='users/doctor_list.html'
    getqueryset = Doctor.objects.all()
    paginate_by = 10
    

class DoctorDetailView(generic.DetailView):
    model = Doctor

class UserListView(generic.ListView):
    model = User
    context_object_name = 'user_list' 
    template_name ='users/user_list.html'
    getqueryset = User.objects.all()
    paginate_by = 10

class UserDetailView(generic.DetailView):
    model = User



class DoctorCreate(CreateView):
    model = Doctor
    fields = ['first_name', 'last_name', 'date_of_birth', 'specification']
   
class DoctorUpdate(UpdateView):
    model = Doctor
    fields = '__all__' # Not recommended (potential security issue if more fields added)
    
class DoctorDelete(DeleteView):
    model = Doctor
    success_url = reverse_lazy('doctors')


class UserCreate(CreateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'username', 'password']
   
class UserUpdate(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'username'] # Not recommended (potential security issue if more fields added)
    
class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('users')
