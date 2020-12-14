from django.contrib import admin

# Register your models here.
from .models import Doctor, Specification, User

#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(Genre)
#admin.site.register(BookInstance)



class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth')
admin.site.register(Doctor, DoctorAdmin)
   
admin.site.register(Specification)

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'username')
admin.site.register(User, UserAdmin)
