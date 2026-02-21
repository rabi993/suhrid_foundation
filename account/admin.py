from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ( 'account_no', 'total_credit', 'total_debit', 'final_cash', 'created_at')
    search_fields = ( 'account_no',)
    list_filter = ('created_at',)
