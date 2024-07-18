from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.urls import reverse

class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    cover_pic = models.ImageField(upload_to='cover_pic', blank=False)
    body = RichTextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self) -> str:
        return f"{self.title} - {self.author}"
    
    def get_absolute_url(self):
        return reverse('portdent_app:post-detail', args=(str(self.id)))