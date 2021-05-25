from django.views import generic
from members.forms import EditProfileForm, PasswordChangingsForm, SignUpForm
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
from django.contrib.auth.forms import   PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView


# Create your views here.

class PasswordsChangeView(PasswordChangeView):
    form_class=PasswordChangingsForm
    success_url = reverse_lazy("password_success")

def password_success(request):
    return render(request,'registration/password_success.html')



class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class UserUpdateProfileView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user

