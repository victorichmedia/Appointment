from django.contrib import admin

# Register your models here.
from .models import CreateAppointment




class CreateAppointmentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'email', 'date', 'time_of_appointment',)
admin.site.register(CreateAppointment, CreateAppointmentAdmin)


