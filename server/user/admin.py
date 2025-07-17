from django.contrib import admin
from .models import UserDetails

# Register your models here.
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'fullname', 'phone_number', 'agent')
    search_fields = ('username', 'email')

admin.site.register(UserDetails, UserDetailsAdmin)
