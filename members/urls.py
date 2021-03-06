from django import views
from django.urls import path
from .views import  PasswordsChangeView, ShowProfilePageView, UserRegisterView, UserUpdateProfileView, EditProfilePageView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("u-register", UserRegisterView.as_view(), name="register"),
    path("edit_profile/", UserUpdateProfileView.as_view(),
         name="edit_profile"),
    path(
        "password/",
    PasswordsChangeView.as_view(
            template_name='registration/change_password.html')),
    path('password_success', views.password_success, name='password_success'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_prfile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page')

]