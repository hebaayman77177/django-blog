from django.urls import path
from .views import UserRegisterView, UserUpdateProfileView

urlpatterns = [
    path("u-register", UserRegisterView.as_view(), name="register"),
    path("edit_profile/", UserUpdateProfileView.as_view(), name="edit_profile"),

]