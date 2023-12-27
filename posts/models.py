from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
    title =  models.CharField(max_length=255)
    content = RichTextField(max_length=30000)
    description = models.TextField(max_length=1500, default="No description")
    picture = models.ImageField(upload_to="picture/", default = "default.jpg")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category =  models.CharField(max_length=255, default='uncategorised')

    class Meta:
          ordering = ('-created_at',)

    def __str__(self):
          return self.title

class UnloggedComment(models.Model):
     post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE, related_name="unloggedComments")
     name = models.CharField(max_length=255)
     email = models.CharField(max_length=255)
     content = models.TextField(max_length=10000)
     created_at = models.DateTimeField(auto_now_add=True)
     APPROVED = 'Approved'
     REJECTED = 'Rejected'
     PENDING = 'Pending'
     STATUS = [
          (APPROVED, 'Approved'),
          (REJECTED, 'Rejected'),
          (PENDING, 'Pending'),
     ]
     status = models.CharField(
          max_length=8,
          choices=STATUS,
          default=PENDING,
     )

     class Meta:
          ordering = ('created_at',)

     def __str__(self):
          return '%s -%s' % (self.post.title, self.name)

class Comment(models.Model):
     post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE, related_name="comments")
     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
     content = models.TextField(max_length=10000)
     created_at = models.DateTimeField(auto_now_add=True)
     APPROVED = 'Approved'
     REJECTED = 'Rejected'
     PENDING = 'Pending'
     STATUS = [
          (APPROVED, 'Approved'),
          (REJECTED, 'Rejected'),
          (PENDING, 'Pending'),
     ]
     status = models.CharField(
          max_length=8,
          choices=STATUS,
          default=PENDING,
     )

     class Meta:
          ordering = ('created_at',)

     def __str__(self):
          return '%s -%s' % (self.post.title, self.created_by)

class Like(models.Model):
     post = models.ForeignKey(Post, blank=True, null=True, on_delete=models.CASCADE)
     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')
     created_at = models.DateTimeField(auto_now_add=True)
