from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("Login/", LoginView.as_view()),
    path("Login/refresh/", TokenRefreshView.as_view()),
    path("SignUp/", SignUpView.as_view()),
]
