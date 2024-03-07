from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from .models import Comment


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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Process the form data, save the comment, etc.
            return redirect('some-view-name')
    else:
        form = CommentForm()
    context = {'form': form}
    return redirect('profile')


# @login_required
def new_building(request):
    context = {}
    return render(request, 'Review/new_building.html', context)


# @login_required
def new_level(request):
    context = {}
    return render(request, 'Review/new_level.html', context)


# @login_required
def new_room(request):
    context = {}
    return render(request, 'Review/new_room.html', context)


from django.shortcuts import render, redirect
from .models import Comment
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    # This view now requires the user to be logged in
    if request.user.is_authenticated:
        user_comments = Comment.objects.filter(user=request.user)
        context = {'comments': user_comments}
        return render(request, 'profile.html', context)
    else:
        return redirect('login')

    return render(request, 'Review/profile.html', context)


# @login_required
def upload_media(request):
    context = {}
    return render(request, 'Review/upload_media.html', context)
