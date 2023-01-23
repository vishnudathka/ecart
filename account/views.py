from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic as views
from account import models
from account import forms
from django.urls import reverse_lazy


class ProfileCreateView(LoginRequiredMixin,views.CreateView) :
    template_name = "account/profile/profile_create.html"
    model = models.ProfileModel
    form_class = forms.ProfileForm
    

    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)    


class ProfileDetailView(LoginRequiredMixin, views.DetailView):
     template_name = "registration/profile.html"
     model =models.ProfileModel
     context_object_name ="profile"

class SignupView(views.CreateView):
    template_name ="registration/signup.html"
    form_class = forms.SignupForm
    success_url = reverse_lazy("account:login")

# Create your views here.
