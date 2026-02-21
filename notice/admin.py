from django.contrib import admin
from .models import Notice
# Register your models here.



@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')
    search_fields = ('name', 'description', 'user__username')
    list_filter = ('created_at',)