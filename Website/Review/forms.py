from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    comment = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class': 'form_control',
            'placeholder': 'Comment here!',
            'rows': 4,
            'cols': 50

        }))
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Comment
        fields = ['comment']
