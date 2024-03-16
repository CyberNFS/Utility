from django.urls import path
from Review import views

app_name = 'Review'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('search/', views.building_search, name='building_search'),

]
