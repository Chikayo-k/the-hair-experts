from .models import Comment
from .models import Comment as Comment, Product
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['review_title','comment_area']
       