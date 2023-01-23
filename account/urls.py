from django.urls import path, include
from account import views


app_name = "account"

urlpatterns = [
     path("", include("django.contrib.auth.urls")),
      path("profile/create/", views.ProfileCreateView.as_view(), name="profile_create"), 
      path("profile/<int:pk>/detail/", views.ProfileDetailView.as_view(), name="profile_detail"),
      path("profile/signup/", views.SignupView.as_view(), name="signup"),

]