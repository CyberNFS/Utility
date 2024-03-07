from django import forms


class CommentForm(forms.Form):
    name = forms.CharField()
    url = forms.URLField()
    comment = forms.CharField(widget=forms.Textarea)


class UserRegistrationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    # Add other fields as necessary

    # Optionally, include email, first_name, last_name, etc.
    email = forms.EmailField()
