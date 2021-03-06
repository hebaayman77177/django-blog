from django import forms
from django.forms import fields, widgets
from .models import Comment, Post, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag","category","author","body","snippet","header_image")


        widgets = {
            "title":
            forms.TextInput(attrs={"class": "form-control"}),
            "title_tag":
            forms.TextInput(attrs={"class": "form-control"}),
            "category":
            forms.Select(attrs={"class": "form-control"}),
            "author":
            forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "create-post-user",
                    "value": "",
                    "type": "hidden",
                }),
            "body":
            forms.Textarea(attrs={"class": "form-control"}),
            "snippet":
            forms.Textarea(attrs={"class": "form-control"})
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "title_tag", "body", "category", "snippet")

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
            "snippet": forms.Textarea(attrs={"class": "form-control"}),

        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name","body")

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }
