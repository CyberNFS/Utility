from django.urls import path
from Review import views

app_name = 'Review'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('search/', views.building_search, name='building_search'),
    path('building_profile/<slug:building_name_slug>/', views.show_building, name = "show_building"),
    path('profile/', views.profile, name='profile'),
    path('gallery/', views.gallery, name = "gallery"),
    path('like_building/', views.LikeBuildingView.as_view(), name = "like_building"),
    path('dislike_building/', views.DislikeBuildingView.as_view(), name = "dislike_building"),

]
