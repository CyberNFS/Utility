from django.contrib import admin
from .models import Profile, Building, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Building)
admin.site.register(Comment)
