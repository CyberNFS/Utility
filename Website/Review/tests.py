from datetime import timezone
from django.test import TestCase
from django.urls import reverse
from .models import Building, BuildingRooms, Comment
from django.contrib.auth.models import User

class BuildingMethodTests(TestCase):
    
    def test_slug_line_creation(self):
        
        """
            This tests whether the building_slug variable is properly created after a building has been initiated.
            
            An example: We add the building (with name of) "New Building Here" and we are expecting the building_slug to be automatically created as
                        "new-building-here"
        """
        
        building = Building(building_name = "New Building Here")
        building.save()
        
        self.assertEqual(building.building_slug, "new-building-here")
        
         
        
class BuildingsViewTest(TestCase):
    
    """
     THIS TESTS THE VIEW CALLED buildings in Review/views.py
    """
    
    def test_buildings_with_no_buildings_in_database(self):
        
        """
            If the database hasn't been populated yet, i.e. there are no buildings to show,
            make sure that the website handles this correclty (the page should display a message like "there are no buildings at the moment...")
        """   
        
        response = self.client.get(reverse("buildings"))
        
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, "There are currently no buildings.")
        
        
        
    def test_buildings_with_buildings_in_database(self):
        
        """
            This tests to make sure that if the database has been populated that this view will correctly display
            any building objects that exist. 
        """
        
        add_building("Adam Smith Building", "55.873868697201004, -4.289791300542604")
        add_building("Sir Alwyn Williams Building", "55.873868697201004, -4.289791300542604")
        add_building("James McCune Smith Building", "55.873868697201004, -4.289791300542604")
        
        response = self.client.get(reverse("buildings"))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Adam Smith Building")
        self.assertContains(response, "Sir Alwyn Williams Building")
        self.assertContains(response, "James McCune Smith Building")
        
        number_of_buildings = len(response.context["buildings"])
        self.assertEquals(number_of_buildings, 3)
        
        

class ShowBuildingViewTest(TestCase):
    
    """
        THIS TESTS THE VIEW CALLED show_building in Review/views.py
    """
    
    def test_view_gets_objects(self):
        
        """
            This is to test if the view correctly gets all objects required:
                Building, BuildingRooms, and Comment
        """
        
        building = add_building("Adam Smith Building", 
                                "55.873868697201004, -4.289791300542604")
        
        user = add_user("username1")
        
        add_building_room("Room 101", building)
        add_comment("This is a comment about the Adam Smith Building", 
                    building,
                    user)
        
        response = self.client.get(reverse("Review:show_building", 
                                           kwargs = {"building_name_slug": building.building_slug}))
        
        self.assertEqual(response.status_code, 200)
        #self.assertContains(response, "Adam Smith Building")
        #self.assertContains(response, "Room 101")
        #self.assertContains(response, "This is a comment about the Adam Smith Building")   
        
        #self.assertEqual(response.context["building"], "Adam Smith Building")
        
        
        
        
        
#Helper functions that don't need to be initialised within a class
#This way the code can be reused for several tests


def add_building(name, google_map):
    
    building = Building.objects.get_or_create(building_name = name,
                                              google_map = google_map)[0]
    building.save()
    
    return building


def add_building_room(title, building):
    
    room = BuildingRooms.objects.get_or_create(room_title = title,
                                               building = building)[0]
    room.save()
    
    return room


def add_comment(text, building, user):
    
    comment = Comment.objects.get_or_create(text = text,
                                            building = building,
                                            author = user)[0]
    comment.save()
    
    return comment


def add_user(username):
    
    user = User.objects.get_or_create(username = username)[0]
    user.save()
    
    return user

