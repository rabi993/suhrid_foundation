from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('trx_id', 'user', 'amount', 'typys', 'created_at')  # Customize fields shown in the list view
    search_fields = ('trx_id', 'user__username')  # Enable search functionality
    list_filter = ('typys', 'created_at')  # Add filters