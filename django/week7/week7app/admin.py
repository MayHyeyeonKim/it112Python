# admin.py
from django.contrib import admin
from week7app.models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ('name', 'type')
    list_display = ('name', 'address', 'type', 'employee')
    list_filter = ('type', 'employee')
