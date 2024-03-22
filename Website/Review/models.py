from django.db import models
from django.utils import timezone
from django.conf import settings
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Building(models.Model):
    
    building_name = models.CharField(max_length=255, unique = True, default = '')
    building_description = models.TextField(default='')
    
    building_image = models.ImageField(upload_to="building_images", blank=True, default = "{{ MEDIA_URL }}building_images/default-image.jpg")
    google_map = models.CharField(max_length=255, default='')
    
    building_instagram = models.URLField(blank = True, default = "https://www.instagram.com/uofglasgow?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==")
    building_website = models.URLField(blank = True)
    
    building_likes = models.IntegerField(default = 0)
    building_dislikes = models.IntegerField(default = 0)

    date_added = models.DateTimeField(default=timezone.now)
    building_slug = models.SlugField(unique = True, default = "")
    
    
    
    def save(self, *args, **kwargs):
        
        self.building_slug = slugify(self.building_name)
        super(Building, self).save(*args, **kwargs)
    
    
    class Meta:
        verbose_name_plural = "Buildings"

    def __str__(self):
        return self.building_name
    
    
    
class BuildingRooms(models.Model):
    
    building = models.ForeignKey(Building, on_delete = models.CASCADE)
    room_title = models.CharField(max_length = 225)
    room_picture = models.ImageField(upload_to = "room_images", blank = True, default = "")
    
    
    
    class Meta:
        verbose_name_plural = "Building Rooms"
    
    def __str__(self):
        return self.room_title


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
            return f'Comment by {self.author.username} on {self.building.building_name}'
        else:
            return f'Comment by {self.author.username} without a building'


class Profile(models.Model):

    name = models.CharField(max_length=80)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile', null=True)
    picture = models.ImageField(
        upload_to="profile_images", blank=True, default = "profile_images/placeholder.jpg")
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
