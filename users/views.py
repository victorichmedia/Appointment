from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from record.models import AppointmentInstance
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib.auth import login, authenticate
from .models import User
from users.forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class AppointmentBookByClientListView(LoginRequiredMixin,generic.ListView):
    model = AppointmentInstance
    template_name ='appointment/appointment_book_by_client.html'
    paginate_by = 10
    
    def get_queryset(self):
        return AppointmentInstance.objects.filter(client=self.request.user)



#User registration

def registration_view(request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data('password')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')
        else:
            form = RegistrationForm()
        return render(request,'users/register.html', {'form' : form })

