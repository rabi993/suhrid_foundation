from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    TRANSACTION_TYPES = [
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    ]

    user = models.CharField(max_length=50, blank=True, null=True) 
    reference = models.CharField(max_length=255, blank=True, null=True)  # Optional Reference
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Transaction amount
    accountNo = models.CharField(max_length=20, blank=True, null=True)  # Account Number
    typys = models.CharField(max_length=10, choices=TRANSACTION_TYPES)  # Transaction Type
    source_people = models.CharField(max_length=255, blank=True, null=True)  # Source of Funds
    purpose = models.TextField(blank=True, null=True)  # Purpose of Transaction
    comment = models.TextField(blank=True, null=True)  # Comments
    approved = models.BooleanField(default=False)  # Approval Status
    

   