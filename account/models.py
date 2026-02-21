from django.db import models
from django.contrib.auth.models import User
import uuid  # For generating unique account numbers

# Account model
class Account(models.Model):
    
    account_no = models.CharField(max_length=20, unique=True, default=uuid.uuid4)  # Unique account number
    total_credit = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Total credited amount
    total_debit = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Total debited amount
    final_cash = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Final cash balance
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the object is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update when the object is saved

    def __str__(self):
        return self.account_no

    def update_final_cash(self):
        """
        Updates the final cash balance based on total_credit and total_debit.
        """
        self.final_cash = self.total_credit - self.total_debit
        self.save()

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
        ordering = ['-created_at']  # Most recent accounts first






