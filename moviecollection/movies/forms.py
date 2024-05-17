from django import forms
from .models import CommentSection

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentSection
        fields = ['message']