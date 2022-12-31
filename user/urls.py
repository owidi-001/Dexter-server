from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (ChangePassword, Register, Login,ProfileUpdate) # , ResetPasswordView, ResetPasswordCompleteView, UserProfileView

urlpatterns = [
    # Auth user
    path("register/", Register.as_view(), name="register"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name="logout"),

    # profile
    path("profile/", ProfileUpdate.as_view(), name="profile"),

    # passwords
    path("password/password_change/", ChangePassword.as_view(), name="change_password"),
]
