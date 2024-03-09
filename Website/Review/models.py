from django.db import models
from django.utils import timezone
from django.conf import settings

from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from django.contrib.auth.models import User


class Building(models.Model):
    # Assuming you have attributes like name for the Building
    name = models.CharField(max_length=255)
    # Add other fields as necessary

    def __str__(self):
        return self.name


class Comment(models.Model):
    # Assuming each comment is related to a Building and a user who posted it
    # building = models.ForeignKey(
    #     Building, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    text = models.TextField()
    date_commented = models.DateTimeField(default=timezone.now)

    def __str__(self):

        return f'Comment by {self.user.username} on {self.building.name}'


class Profile(models.Model):

    profile_ID = models.CharField(max_length=100, unique=True)
    user_ID = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=80)

    picture = models.ImageField(upload_to="profile_images", blank=True)
    upvotes = models.IntegerField(default=0)
    images = models.ImageField(upload_to="", blank=True)
    bio = models.CharField(max_length=100)
    reviews = models.CharField(max_length=1000)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.author.username} : {self.title}'


class Building(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    image = models.ImageField(
        upload_to="building_images", blank=True, null=True)
    google_map = models.CharField(max_length=255, default='')
    instagram = models.CharField(max_length=255, default='')
    website = models.CharField(max_length=255, default='')
    # Allowing null for image field

    date_added = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(unique=True, blank=True, default='')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
