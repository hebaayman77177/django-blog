from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from .models import Post
from .forms import PostForm

# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "home.html"


class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
