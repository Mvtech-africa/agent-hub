from django.contrib import admin
from .models import Property

class AdminProperty(admin.ModelAdmin):
    list_display = ('title', 'price', 'agent')
    search_fields = ('title', 'description')
    list_filter = ('agent',)
# Register your models here.
admin.site.register(Property, AdminProperty)
