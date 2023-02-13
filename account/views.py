from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic as views
from account import models
from account import forms
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views
from django.conf import settings
import requests


class ProfileCreateView(LoginRequiredMixin, views.CreateView):
    template_name = "account/profile/profile_create.html"
    model = models.ProfileModel
    form_class = forms.ProfileForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileDetailView(LoginRequiredMixin, views.DetailView):
    template_name = "registration/profile.html"
    model = models.ProfileModel
    context_object_name = "profile"


class SignupView(views.CreateView):
    template_name = "registration/signup.html"
    form_class = forms.SignupForm
    success_url = reverse_lazy("account:login")


# class LoginView(views.FormView):
#     template_name = "registration/login.html"
#     form_class =auth_forms.AuthenticationForm
#     def form_valid(self, form):
#         credential = form.clean()
#         username = credential['username']
#         password = credential['password']
#         user =authenticate(self.request,username=username,password=password)
#         if user is not None:
#             login(self.request,user)
#             return redirect(reverse_lazy(settings.LOGIN_REDIRECT_URL))

#         return super().form_invalid(form)


class CustomLoginView(auth_views.LoginView):
    redirect_login_user = True
    enable_recaptcha = True
    extra_context = {"g_recaptcha_site_key": settings.GOOGLE_RECAPTCHA_SITE_KEY}

    def form_valid(self, form):
        g_recaptcha_response = self.request.POST.get("g-recaptcha-response")

        if self.enable_recaptcha:
            data = {
                "secret": settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                "response": g_recaptcha_response,
            }
            response = requests.post(
                settings.GOOGLE_RECAPTCHA_VERIFY_URL, data=data
            ).json()
            verified = response.get("success")
            if not verified:
                return super().form_invalid(form)
        return super().form_valid(form)


class LogoutView(views.View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy(settings.LOGIN_URL))


# Create your views here.
