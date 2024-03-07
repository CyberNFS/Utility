from django.db import models
from django.conf import settings


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
