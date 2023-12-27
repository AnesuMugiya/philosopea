from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     image = models.ImageField(default='default.jpg', upload_to='profile_pics')
     READER = 'Moderator'
     MODERATOR = 'Moderator'
     EDITOR = 'Editor'
     ACCOUNT = [
          (READER, 'Moderator'),
          (MODERATOR, 'Moderator'),
          (EDITOR, 'Editor'),
     ]
     account = models.CharField(
          max_length=9,
          choices=ACCOUNT,
          default=READER,
     )

     def __str__(self):
          return f'{self.user.username} Profile'

     # class for resizing large images owo
     def save(self, *args, **kwargs):
          super().save(*args, **kwargs)

          img = Image.open(self.image.path)

          if img.height > 300 or img.width > 300:
               output_size = (300,300)
               img.thumbnail(output_size)
               # saves the image to the file path overiding the image
               img.save(self.image.path) 

# Look up how to crop images

User.users = property(lambda u:Profile.objects.get_or_create(user=u)[0])
# Lambda makes it possible to create user when they sign up



