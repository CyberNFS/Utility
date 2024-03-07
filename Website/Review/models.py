from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User



class Building(models.Model):
    # Assuming you have attributes like name for the Building
    name = models.CharField(max_length=255)
    # Add other fields as necessary

    def __str__(self):
        return self.name


class Comment(models.Model):
    # Assuming each comment is related to a Building and a user who posted it
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'Comment by {self.user.username} on {self.building.name}'
    


class Profile(models.Model):

    profile_ID = models.CharField(max_length = 100, unique = True)
    user_ID = models.CharField(max_length = 100, unique = True)
    name = models.CharField(max_length = 80)

    picture = models.ImageField(upload_to = "profile_images", blank = True)
    upvotes = models.IntegerField(default = 0)
    images = models.ImageField(upload_to = "", blank = True)
    bio = models.CharField(max_length = 100)
    reviews = models.CharField(max_length = 1000)


