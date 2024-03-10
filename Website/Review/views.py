from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth import login as auth_login
from .forms import CommentForm, RegistrationForm, BuildingForm
from .models import Comment, Building, Profile
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    context = {}
    return render(request, 'Review/home.html', context)


def buildings(request):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            # Ensure 'building_id' is captured and validated before this step
            building_id = request.POST.get('building_id')
            if building_id:
                try:
                    new_comment.building = Building.objects.get(id=building_id)
                    new_comment.save()
                    return redirect('buildings')
                except Building.DoesNotExist:
                    # Handle the case where building does not exist
                    pass
    else:
        comment_form = CommentForm()
    buildings = Building.objects.all()
    context = {'comment_form': comment_form, 'buildings': buildings}
    return render(request, 'Review/buildings.html', context)


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
    # Redirect to a success page.
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                # Include other fields as needed
                email=form.cleaned_data['email']
            )
            new_user.save()
            # Log the user in and redirect them
            login(request, new_user)
            # Redirect to a new page after registration
            return redirect('profile')
    else:
        form = RegistrationForm()

    return render(request, 'Review/register.html', {'form': form})


def gallery(request):
    context = {}
    return render(request, 'Review/gallery.html', context)


def building_profile(request, slug):
    building = get_object_or_404(Building, slug=slug)
    context = {
        'building': building,
        # 'comments': comments,  # Uncomment if you're including comments
    }
    return render(request, 'Review/building_profile.html', context)


def new_building(request):
    if request.method == 'POST':
        form = BuildingForm(request.POST, request.FILES)
        if form.is_valid():
            building = form.save(commit=False)
            # You can add additional processing here if needed
            building.save()
            return redirect('buildings')
    else:
        form = BuildingForm()
    return render(request, 'Review/new_building.html', {'form': form})


# @login_required
def new_level(request):
    context = {}
    return render(request, 'Review/new_level.html', context)


# @login_required
def new_room(request):
    context = {}
    return render(request, 'Review/new_room.html', context)


def profile(request):
    # Fetch the comments made by the user and their related profiles

    user_comments = Comment.objects.select_related(
        'author__profile').filter(author=request.user)
    context = {"comments": user_comments}
    return render(request, 'Review/profile.html', context)

    # This view now requires the user to be logged in
    # if request.user.is_authenticated:
    # user_comments = Comment.objects.filter(user=request.user)
    # context = {'comments': user_comments}
    # return render(request, 'profile.html', context)
    # else:
    # return redirect('login')

    # return render(request, 'Review/profile.html', context)


# @login_required
def upload_media(request):
    context = {}
    return render(request, 'Review/upload_media.html', context)


def comment(request):
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # validity check
        if form.is_valid():
            form.save(commit=True)
            return redirect('/home/')
        else:
            print(form.errors)
    return render(request, 'Review/comment.html', {'form': form})


def about(request):
    return render(request, 'Review/about.html')
