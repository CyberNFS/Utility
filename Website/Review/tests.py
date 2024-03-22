from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from .models import Building, BuildingRooms, Comment, Profile
from django.contrib.auth.models import User


class BuildingMethodTests(TestCase):
    
    """
        These are tests for the Building MODEL in Review/models.py
    """
    
    def test_slug_line_creation(self):
        
        """
            This tests whether the building_slug variable is properly created after a building has been initiated.
            
            An example: We add the building (with name of) "New Building Here" and we are expecting the building_slug to be automatically created as
                        "new-building-here"
        """
        
        building = Building(building_name = "New Building Here")
        building.save()
        
        self.assertEqual(building.building_slug, "new-building-here")
        
        
    def test_building_creation_stores_all_variables_correctly(self):
        
        """
            This tests that when a new Building object is created that is successfully stores all of its variables:
            
                building_name, building_description_, building_instagram, building_website, building_image, google_map
                            
                building_likes, building_dislikes (these two are default values, so no need to initate them as that is what we want to test)
        """
        
        building = Building(building_name = "JMS Building",
                            building_description = "This is a new building on campus.",
                            building_instagram = "https://www.instagram.com",
                            building_website = "https://www.moodle.gla.ac.uk",
                            google_map = "55.02, -4.567")
        
        building.save()
        
        self.assertEqual(building.building_description, "This is a new building on campus.")
        self.assertEqual(building.building_name, "JMS Building")
        self.assertEqual(building.building_instagram, "https://www.instagram.com")
        self.assertEqual(building.building_website, "https://www.moodle.gla.ac.uk")
        self.assertEqual(building.google_map, "55.02, -4.567")
        
        self.assertEqual(building.building_likes, 0)
        self.assertEqual(building.building_dislikes, 0)
        
         
        
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
        
        The BuildingRooms model is only utilised within this view as well, so this will
        also make tests to show that the Buildingrooms model will correctly display within a view.
    """
    
    def test_view_gets_objects(self):
        
        """
            This is to test if the view correctly gets all objects required:
                Building, BuildingRooms, and Comment
                
            And tests that the google_map variable is correctly split up
        """
        
        building = add_building("Adam Smith Building", 
                                "55.873868697201004, -4.289791300542604")
        
        latitude, longitude = building.google_map.replace(" ", "").split(",")
        
        user = add_user("username1")
        
        add_building_room("Room 101", building)
        add_comment("This is a comment about the Adam Smith Building", 
                    building,
                    user)
        
        response = self.client.get(reverse("Review:show_building", 
                                           kwargs = {"building_name_slug": building.building_slug}))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Adam Smith Building")
        self.assertContains(response, "Room 101")
        self.assertContains(response, "This is a comment about the Adam Smith Building")   
        
        self.assertEqual(response.context["building"], building)
        self.assertEqual(response.context["latitude"], latitude)
        self.assertEqual(response.context["longitude"], longitude)
    
    
    
    def test_response_if_no_comments_added(self):
        
        """
            This tests that when the wbesite loads this page from the correct path that
            if there are no comments been added to the building, the page will show the appropriate message
            and not cause the website to crash or have any errors
        """
        
        building = add_building("I am a building", "1234, -234")
        
        response = self.client.get(reverse("Review:show_building",
                                           kwargs = {"building_name_slug": building.building_slug}))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are currently no comments for this building.")
        
        
    def test_no_rooms_allocated_to_building_response(self):
        
        """
            This tests that if no rooms have been added to the building that the view
            will show, that it will display an appropriate message to indicate this and not
            cause any errors or crashes for the website.
        """
        
        building = add_building("I am a building", "123, 456")
        
        response = self.client.get(reverse("Review:show_building",
                                    kwargs = {"building_name_slug": building.building_slug}))
        
        self.assertContains(response, "This building has no rooms or none have been added yet.")      
        



class BuildingRoomsTest(TestCase):
    
    def test_room_creation_successful(self):
        
        """
            This tests the MODEL BuildingRooms to make sure that objects are created successfully.
            This model has a foreign key for a building, a char_field for it's title and a picture.
        """
        
        building = Building(building_name = "Sir Building")
        building.save()
        
        room = BuildingRooms(room_title = "Room 207", room_picture = "file_dir/room_image.jpg", building = building)
        room.save()
        
        self.assertEqual(building.building_name, "Sir Building")
        self.assertEqual(room.room_title, "Room 207")
        self.assertEqual(room.room_picture, "file_dir/room_image.jpg")
        self.assertEqual(room.building, building)



class ProfileTest(TestCase):

    """
        This tests the MODEL Profile in Review/models.py
    """

    def test_profile_creates_objects_successfully(self):

        """
            This tests to make sure that the Profile model successfully creates objects.
        """

        user = add_user("Robert Smith")

        profile = Profile(name = "Robert Smith",
                          picture = "file_dir/profile_images/profile.jpg",
                          bio = "I am Robert.",
                          reviews = "This is a review",
                          user = user)
        

        self.assertEqual(profile.name, "Robert Smith")
        self.assertEqual(profile.picture, "file_dir/profile_images/profile.jpg")
        self.assertEqual(profile.bio, "I am Robert.")
        self.assertEqual(profile.reviews, "This is a review")
        self.assertEqual(profile.user, user)
        
      

class CommentTest(TestCase):

    """
        This tests the MODEL Comment in Review/models.py
    """  

    def test_comment_creates_objects_successfully(self):

        """
            This makes sure that the Comment model successfully creates new objects
            of Comment type.
        """

        user = add_user("Smith Robert")
        building = add_building("Robert Smith Building", "222, -222")

        date_commented = timezone.now

        comment = Comment(author = user,
                          text = "this is a comment by Smith Robert",
                          building = building,
                          date_commented = date_commented)
        

        self.assertEqual(comment.author, user)
        self.assertEqual(comment.building, building)
        self.assertEqual(comment.text, "this is a comment by Smith Robert")
        self.assertEqual(comment.date_commented, date_commented)
        
        
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

