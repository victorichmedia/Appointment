from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse

# Create your models here.
class CreateAppointment(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField('email', blank=True)
    time_of_appointment = models.TimeField()
    date = models.DateField()

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name}'
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this appointment."""
        return reverse('appointment_detail', args=[str(self.id)])


class AppointmentInstance(models.Model):
    """ Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    appointment = models.ForeignKey('CreateAppointment', on_delete=models.SET_NULL, null=True) 


    APPOINTMENT_STATUS = (
        ('Approved', 'Approved'),
        ('Canceled', 'Canceled'),
        ('Pending', 'Pending'),
    )
      
    status = models.CharField(
        max_length=20,
        choices=APPOINTMENT_STATUS,
        blank=True,
        default='Pending',
    )

 
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.appointment})'