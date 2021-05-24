from django.shortcuts import get_object_or_404, render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy, reverse
from .models import Category, Post
from .forms import PostForm, EditPostForm, CategoryForm
from django.http import HttpResponseRedirect

# Create your views here.
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_details', args=[str(pk)]))
    

def CategoryView(request, category_name):
    category_name=category_name.replace("-", " ")
    category = Category.objects.get(name=category_name)
    print(category)
    posts = Post.objects.filter(category=category)
    print(posts)
    context = {"category": category, "posts": posts}
    return render(request, "categories.html", context)


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ["-post_date"]


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

# todo make the category when saved be small case
class AddCategoryView(CreateView):
    model = Post
    form_class = CategoryForm
    template_name = "category_form/add.html"
    success_url = reverse_lazy("home")

