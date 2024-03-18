from django.contrib import admin
from .models import Profile, Building, BuildingRooms, Comment


class BuildingRoomsAdmin(admin.ModelAdmin):
    
    list_display = ("room_title", "building")
    
    
class BuildingAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {"building_slug": ("building_name",)}
    

# Register your models here.
admin.site.register(Profile)
admin.site.register(Building, BuildingAdmin)
admin.site.register(BuildingRooms, BuildingRoomsAdmin)
admin.site.register(Comment)
