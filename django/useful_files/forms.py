# myapp/forms.py
from django import forms
from .models import Articles

class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text']
