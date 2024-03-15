from django.db import models
from django.utils import timezone
from django.conf import settings
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



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
        return f"{self.name} - {self.description}"


class Comment(models.Model):
    # Assuming each comment is related to a Building and a user who posted it
    # building = models.ForeignKey(
    #     Building, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    text = models.TextField()
    date_commented = models.DateTimeField(default=timezone.now)
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, related_name='comments', null=True)

    def __str__(self):
        if self.building is not None:
            return f'Comment by {self.author.username} on {self.building.name}'
        else:
            return f'Comment by {self.author.username} without a building'


class Profile(models.Model):

    # profile_ID = models.CharField(max_length=100, unique=True)
    # user_ID = models.CharField(max_length=100, unique=True)
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile', null=True) 
    #I think this line of code already indicates the foreign key and will do the auto-matching, so no need for user_id
    name = models.CharField(max_length=80)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile', null=True)
    picture = models.ImageField(
        upload_to="profile_images", blank=True, default=f'Website/mediacat.jpg')
    upvotes = models.IntegerField(default=0)
    images = models.ImageField(upload_to="", blank=True)
    bio = models.CharField(max_length=100)
    reviews = models.CharField(max_length=1000)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} Profile'


def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
