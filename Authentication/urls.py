from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("login/", LoginView.as_view()),
    path("login/refresh/", TokenRefreshView.as_view()),
    path("signup/", SignUpView.as_view()),
    path("logout/", LogOutView.as_view()),
    path("htmldoc/", Doc),
]