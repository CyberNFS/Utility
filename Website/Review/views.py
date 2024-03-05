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


def building_profile(request):
    context = {}
    return render(request, 'Review/building_profile.html', context)


@login_required
def new_building(request):
    context = {}
    return render(request, 'Review/new_building.html', context)


@login_required
def new_level(request):
    context = {}
    return render(request, 'Review/new_level.html', context)


@login_required
def new_room(request):
    context = {}
    return render(request, 'Review/new_room.html', context)


@login_required
def profile(request):
    context = {}
    return render(request, 'Review/profile.html', context)


@login_required
def upload_media(request):
    context = {}
    return render(request, 'Review/upload_media.html', context)
