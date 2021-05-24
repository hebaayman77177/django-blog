from django.contrib import admin
from django.urls import path, include
from .views import (
    HomeView,
    PostDetailView,
    AddPostView,
    EditPostView,
    DeletePostView,
    AddCategoryView,
    CategoryView,
    LikeView
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("add-post", AddPostView.as_view(), name="add-post"),
    path("post/edit/<int:pk>", EditPostView.as_view(), name="edit-post"),
    path("post/delete/<int:pk>", DeletePostView.as_view(), name="delete-post"),
    path("add-category", AddCategoryView.as_view(), name="add-category"),
    path("category/<str:category_name>", CategoryView, name="category-detail"),
    path("like/<int:pk>", LikeView, name="like_post"),
]
