from django.db import models
from django.contrib.auth.models import User
from people.models import People
from category.models import Category
from django.core.exceptions import ValidationError

class Post(models.Model):
    user = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, unique=True)
    content = models.TextField()
    image = models.URLField(max_length=500, blank=True, null=True) 
    category = models.ManyToManyField(Category)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title 

    class Meta:
        # unique_together = ('title', 'category')
        # unique ='title'
        verbose_name_plural = "Posts"
        ordering = ['-created_at']


class Comment(models.Model):
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)  # User is already the commentor
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Commentor: {self.commentor.first_name}; Post: {self.post.title}"  # Updated

    class Meta:
        verbose_name_plural = "Comments"

