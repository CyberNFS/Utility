"""Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Review import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Review/', include('Review.urls')),
    path('', views.home, name='home'),
    path('buildings/', views.buildings, name='buildings'),
    
    path('building/<slug:building_name_slug>/', views.show_building, name = "show_building"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    
    path('gallery/', views.gallery, name='gallery'),
    
    path('new_building/', views.new_building, name='new_building'),
    path('building/', views.building_profile, name='building_profile'),
    
    path('new_level/', views.new_level, name='new_level'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit_profile', views.edit_profile, name='edit_profile'),
    path('upload_media/', views.upload_media, name='upload_media'),
    
    
    path('register/', views.register, name='register'),
    path('comment/', views.comment, name='comment'),
    path('about/', views.about, name='about'),
    
    path('search/', views.building_search, name='building_search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
