from django.contrib import admin

# Register your models here.

from week6_app.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['lastname', 'firstname', 'date_of_birth', 'phone',
                    'city', 'zip', 'state', 'graduation', 'email', 'year']
    list_filter = ['lastname', 'firstname', 'date_of_birth', 'phone',
                   'city', 'zip', 'state', 'graduation', 'email', 'year']
    search_fields = ['lastname', 'firstname', 'date_of_birth', 'phone',
                     'city', 'zip', 'state', 'graduation', 'email', 'year']


admin.site.register(Student, StudentAdmin)