from myblog.models import Profile
from django.db import models
from django.views import generic
from members.forms import EditProfileForm, PasswordChangingsForm, SignUpForm
from django.shortcuts import get_object_or_404, render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from django.contrib.auth.views import PasswordChangeView

# Create your views here.


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = [
        'bio', 'profile_pic', 'website_url', 'fb_url', 'instgram_url',
        'twitter_url', 'pintrest_url'
    ]
    success_url = reverse_lazy("home")


class ShowProfilePageView(DeleteView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView,
                        self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingsForm
    success_url = reverse_lazy("password_success")


def password_success(request):
    return render(request, 'registration/password_success.html')


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
