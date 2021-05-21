from django.urls import path
from .views import UserRegisterView

urlpatterns = [
    path("u-register", UserRegisterView.as_view(), name="register"),
]