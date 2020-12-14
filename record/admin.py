from django.contrib import admin

# Register your models here.
from .models import CreateAppointment, AppointmentInstance

#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(Genre)
#admin.site.register(BookInstance)



class CreateAppointmentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'email', 'date', 'time_of_appointment',)
admin.site.register(CreateAppointment, CreateAppointmentAdmin)

@admin.register(AppointmentInstance)
class AppointmentInstanceAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'client', 'status')
    fieldsets = (
    ('Availability', {
        'fields': ('appointment','client','status',)
    }),
)

