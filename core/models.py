from django.db import models

# Create your models here.
class Message(models.Model):
     name = models.CharField(max_length=255)
     email = models.CharField(max_length=255)
     content = models.TextField(max_length=10000)
     created_at = models.DateTimeField(auto_now_add=True)

     class Meta:
          ordering = ('created_at',)
