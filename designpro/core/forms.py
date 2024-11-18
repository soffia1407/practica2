from django import forms
from .models import Request, Category

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['title', 'description', 'category', 'photo']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
