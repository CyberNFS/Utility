from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def home(request):
    context = {}
    return render(request, 'Review/home.html', context)


def buildings(request):
    context = {}
    return render(request, 'Review/buildings.html', context)


def login(request):
    context = {}
    return render(request, 'Review/login.html', context)


def register(request):
    context = {}
    return render(request, 'Review/register.html', context)


def gallery(request):
    context = {}
    return render(request, 'Review/gallery.html', context)
