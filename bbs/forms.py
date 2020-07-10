from django import forms
from .models import Article

class SearchForm(forms.Form):
        class Meta:
            model = Article
            fields = ('content', 'user_name')