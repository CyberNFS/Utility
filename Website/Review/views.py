from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth import login as auth_login
from .forms import CommentForm, RegistrationForm
from .models import Comment
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    context = {}
    return render(request, 'Review/home.html', context)


def buildings(request):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():

            Comment.objects.create(
                user=request.user,
                text=comment_form.cleaned_data['comment'],
                building_id=comment_form.cleaned_data['building_id']
            )
            return redirect('buildings')
    else:
        comment_form = CommentForm()

    context = {'comment_form': comment_form}
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


#@login_required
def profile(request):

    #user_comments = Comment.objects.filter(user = request.user)
    #context = {"comments": user_comments}

    return render(request, 'Review/profile.html')

    # This view now requires the user to be logged in
    # if request.user.is_authenticated:
    #user_comments = Comment.objects.filter(user=request.user)
    #context = {'comments': user_comments}
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
