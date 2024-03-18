from django import forms
from .models import Comment, Building, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'picture', 'bio', 'reviews']
        # labels = {
        #     'name': 'Full Name',
        #     'picture': 'Profile Picture',
        #     'bio': 'Bio',
        #     'reviews': 'Reviews',
        # }
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }


class CommentForm(forms.ModelForm):
    text = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class': 'form_control',
            'placeholder': 'Comment here!',
            'rows': 4,
            'cols': 50

        }))
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Comment
        fields = ['text', 'likes']


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'password1', 'password2',)

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user


class BuildingForm(forms.ModelForm):
    
    building_name = forms.CharField(max_length = 128, help_text = "Please enter the building's name.")
    building_slug = forms.CharField(widget = forms.HiddenInput(), required = False)
    
    building_image = forms.ImageField()
    google_map = forms.CharField(max_length = 255, help_text = "Please insert the coordinates from a google map of the building.")
    
    building_website = forms.URLField(help_text = "Please enter the complete URL of the page.")
    building_instagram = forms.URLField(help_text = "Please enter the complete url of the instagram page")
    
    building_views = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    building_likes = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
    
    building_description = forms.CharField(max_length = 225)
    
    class Meta:
        
        model = Building
        fields = ('building_name', )
        
        
class BuildingSearchForm(forms.Form):
    q = forms.CharField(
        required=False, 
        label='Search Buildings', 
        widget=forms.TextInput(attrs={'placeholder': 'Search...'})
    )
