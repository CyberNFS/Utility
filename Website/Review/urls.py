from django.urls import path
from Review import views

app_name = 'Review'

urlpatterns = [
    path('', views.home, name='home'),
]
