from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notice(models.Model):
    user = models.CharField(max_length=50, blank=True, null=True) 
    name = models.CharField(max_length=100)  # Name/title of the notice
    description = models.TextField()  # Detailed description of the notice
    file = models.URLField(max_length=500, blank=True, null=True)  # Optional file (e.g., link to a document)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the notice is created

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Notice"
        verbose_name_plural = "Notices"
        ordering = ['-created_at']  # Orders notices by the most recent first

from django.contrib.auth.models import User    

class noticeComment(models.Model):
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)  # User is already the commentor
    post = models.ForeignKey(Notice, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Commentor: {self.commentor.first_name}; Post: {self.post.name}"  # Updated

    class Meta:
        verbose_name_plural = "noticeComments"