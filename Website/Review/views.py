import os
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth import login as auth_login
from .forms import CommentForm, RegistrationForm, BuildingForm, ProfileForm, RoomForm, BuildingSearchForm
from .models import Comment, Building, Profile, BuildingRooms
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Prefetch, Q, Count, Max
from django.utils.decorators import method_decorator
from django.views import View
from django.urls import reverse
from django.conf import settings


def home(request):
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            building_id = request.POST.get('building_id')
            try:
                new_comment.building = Building.objects.get(id=building_id)
                new_comment.save()
            except Building.DoesNotExist:
                pass
            return redirect('buildings')
    else:
        comment_form = CommentForm() if request.user.is_authenticated else None
    top_liked_buildings = Building.objects.annotate(
        like_count=Count('building_likes')).order_by('-like_count')[:3]
    try:
        recent_comment = Comment.objects.latest('date_commented')
        recent_commented_building = recent_comment.building
    except Comment.DoesNotExist:
        recent_comment = None
        recent_commented_building = None

    for building in top_liked_buildings:
        building.image_url = building.building_image.url if building.building_image else None

    if recent_commented_building:
        recent_commented_building.image_url = recent_commented_building.building_image.url if recent_commented_building.building_image else None
        recent_comment.image_url = recent_comment.author.profile.picture.url if recent_comment.author.profile.picture else None
    context = {
        "isactive": "home",
        "top_liked_buildings": top_liked_buildings,
        "recent_comment": recent_comment,
        "recent_commented_building": recent_commented_building,
        'comment_form': comment_form if request.user.is_authenticated else None,
    }
    return render(request, 'Review/home.html', context)


def buildings(request):
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            building_id = request.POST.get('building_id')
            try:
                new_comment.building = Building.objects.get(id=building_id)
                new_comment.save()
            except Building.DoesNotExist:
                pass
            return redirect('buildings')
    else:
        comment_form = CommentForm() if request.user.is_authenticated else None

    keywords = request.GET.get('keyword')
    if keywords:
        buildings_query = Building.objects.filter(
            Q(building_name__icontains=keywords) |
            Q(building_description__icontains=keywords) |
            Q(google_map__icontains=keywords) |
            Q(building_instagram__icontains=keywords) |
            Q(building_website__icontains=keywords)
        )
    else:
        buildings_query = Building.objects.all()

    buildings = buildings_query.prefetch_related(
        Prefetch(
            'comments',
            queryset=Comment.objects.order_by('-date_commented'),
            to_attr='recent_comments'
        )
    )

    context = {
        'comment_form': comment_form if request.user.is_authenticated else None,
        'buildings': buildings,
        "isactive": "buildings"
    }

    return render(request, 'Review/buildings.html', context)


def building_profile(request, slug):
    building = get_object_or_404(Building, slug=slug)
    context = {
        'building': building,
        'comments': comments,
    }
    return render(request, 'Review/building_profile.html', context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'Review/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            new_user.save()
            login(request, new_user)
            return redirect('Review:profile')
    else:
        form = RegistrationForm()

    return render(request, 'Review/register.html', {'form': form})


def gallery(request):
    context = {"isactive": "gallery"}
    return render(request, 'Review/gallery.html', context)


@login_required
def new_building(request):
    if request.method == 'POST':
        form = BuildingForm(request.POST, request.FILES)
        if form.is_valid():
            building = form.save(commit=False)
            building.google_map = request.POST.get('google_map')
            building.building_image = request.FILES.get('building_image')
            building.building_description = request.POST.get(
                'building_description')
            building.building_website = request.POST.get("building_website")
            # You can add additional processing here if needed
            building.save()
            return redirect('buildings')
    else:
        form = BuildingForm()
    return render(request, 'Review/new_building.html', {'form': form})


@login_required
def new_level(request):

    if request.method == "POST":
        form = RoomForm(request.POST, request.FILES)

        if form.is_valid():
            room = form.save(commit=False)
            room.room_title = request.POST.get("room_title")
            room.picture = request.FILES.get("room_picture")
            room.save()

            return redirect("buildings")

    else:
        form = RoomForm()

    return render(request, "Review/new_level.html", {"form": form})


@login_required
def profile(request):
    context_dict = {}

    user_comments = Comment.objects.select_related(
        'author__profile').filter(author=request.user)

    try:
        profile = request.user.profile

    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    finally:
        context_dict["profile"] = profile

    context_dict["comments"] = user_comments

    return render(request, 'Review/profile.html', context_dict)


@login_required
def edit_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,
                           instance=request.user.profile)
        if form.is_valid():
            form.save()
            # Redirect to the profile page or any other page
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'Review/edit_profile.html', {'form': form})


@login_required
def upload_media(request):
    context = {}
    return render(request, 'Review/upload_media.html', context)


@login_required
def comment(request):
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # validity check
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.save()
            return redirect('/home/')
        else:
            print(form.errors)
    return render(request, 'Review/comment.html', {'form': form})


def about(request):
    return render(request, 'Review/about.html')


def building_search(request):
    form = BuildingSearchForm(request.GET)
    results = None
    search_performed = False  # Flag to indicate if a search was performed

    if 'q' in request.GET:
        search_performed = True  # Update the flag when a search is performed
        if form.is_valid():
            query = form.cleaned_data['q']
            if query:
                results = Building.objects.filter(
                    Q(building_name__icontains=query) |
                    Q(building_description__icontains=query) |
                    Q(google_map__icontains=query) |
                    Q(building_instagram__icontains=query) |
                    Q(building_website__icontains=query)
                )
            else:
                results = Building.objects.all()

    context = {
        'form': form,
        'results': results,
        'search_performed': search_performed
    }
    return render(request, 'Review/search_results.html', context)


def show_building(request, building_name_slug):

    context_dict = {}

    try:

        building = Building.objects.get(building_slug=building_name_slug)

        rooms = BuildingRooms.objects.filter(building=building)

        comments = building.comments.all()

        context_dict["comments"] = comments
        context_dict["rooms"] = rooms
        context_dict["building"] = building

        latitude, longitude = building.google_map.replace(" ", "").split(',')
        context_dict["latitude"] = latitude
        context_dict["longitude"] = longitude

    except Building.DoesNotExist:

        context_dict["building"] = None
        context_dict["rooms"] = None

    return render(request, 'Review/building_profile.html', context=context_dict)


def gallery(request):
    buildings = Building.objects.all()
    return render(request, 'Review/gallery.html', {'buildings': buildings})


class LikeBuildingView(View):

    @method_decorator(login_required)
    def get(self, request):

        building_name = request.GET['building_name']

        try:
            building = Building.objects.get(building_name=building_name)

        except Building.DoesNotExist:
            return HttpResponse(-1)

        except ValueError:
            return HttpResponse(-1)

        building.building_likes += 1
        building.save()

        return HttpResponse(building.building_likes)


class DislikeBuildingView(View):

    @method_decorator(login_required)
    def get(self, request):

        building_name = request.GET['building_name']

        try:
            building = Building.objects.get(building_name=building_name)

        except Building.DoesNotExist:
            return HttpResponse(-1)

        except ValueError:
            return HttpResponse(-1)

        building.building_dislikes += 1
        building.save()

        return HttpResponse(building.building_dislikes)
