from django import forms
from .models import Post, Category


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text", "category")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
        }


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text", "category")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"})
        }


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
