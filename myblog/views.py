from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm, EditPostForm

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-post_date']


class PostDetailView(DetailView):
    model = Post
    template_name = "post_details.html"


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "post_form/add_post.html"


class EditPostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = "post_form/update_post.html"


class DeletePostView(DeleteView):
    model = Post
    # form_class = EditPostForm
    template_name = "post_form/delete_post.html"
    success_url = reverse_lazy("home")
