from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta

# Create your models here.
class People(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to the User model
    image = models.URLField(max_length=500, blank=True, null=True)  # Optional profile image
    mobile_no = models.CharField(max_length=15)  # Mobile number (max length increased for international numbers)
    
    # Additional fields
    birth_date = models.DateField(blank=True, null=True)
    union = models.CharField(max_length=255, blank=True, null=True)  # Union/area information
    word = models.CharField(max_length=255, blank=True, null=True)  # Country or global location
    village = models.CharField(max_length=255, blank=True, null=True)  # Village information
    blood_group = models.CharField(
        max_length=4, 
        choices=[('A+', 'A+'), ('A-', 'A-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-')], 
        blank=True,
        null=True
    )
    last_blood_donate_date = models.DateField(blank=True, null=True)
    available_for_donate_date = models.DateField(blank=True, null=True) 
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        blank=True,
        null=True
    )  # Gender choices
    marital_status = models.CharField(
        max_length=10,
        choices=[('Single', 'Single'), ('Married', 'Married'), ('Separated', 'Separated'), ('Divorced', 'Divorced')], 
        blank=True,
        null=True
    )  # Marital status
    designation = models.CharField(max_length=255, blank=True, null=True)  # Job designation
    worksat = models.CharField(max_length=255, blank=True, null=True)  # Workplace
    livesIn = models.CharField(max_length=255, blank=True, null=True)  # Current residence
    varsity = models.CharField(max_length=255, blank=True, null=True)  # University attended
    session = models.CharField(max_length=20, blank=True, null=True)  # Academic session (e.g., 2015-2019)
    complete = models.BooleanField(default=False)  # Indicates whether studies are complete
    subject = models.CharField(max_length=255, blank=True, null=True)  # Field of study/subject
    association_post = models.CharField(max_length=255, blank=True, null=True)  # Association/organization post
    cv = models.URLField(max_length=500, blank=True, null=True)  # URL to CV/resume


    
    def save(self, *args, **kwargs):
        if self.last_blood_donate_date:
            self.available_for_donate_date = self.last_blood_donate_date + timedelta(days=90)
        else:
            self.available_for_donate_date = None
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        verbose_name_plural = "People"
