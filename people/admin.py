from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'mobile_no', 'union','word','village', 'blood_group', 'gender', 'marital_status', 'worksat')
    search_fields = ('user__username', 'mobile_no', 'worksat')
    list_filter = ('gender', 'marital_status', 'blood_group', 'complete')

    def first_name(self, obj):
        return obj.user.first_name
    
    def last_name(self, obj):
        return obj.user.last_name
    
    def email(self, obj):
        return obj.user.email

    # Add verbose names for custom methods
    first_name.short_description = 'First Name'
    last_name.short_description = 'Last Name'
    email.short_description = 'Email'