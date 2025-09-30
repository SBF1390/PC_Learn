from django.shortcuts import render
from drf_spectacular.utils import (
    extend_schema,
    inline_serializer,
    OpenApiResponse,
    OpenApiParameter,
)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from .models import *
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from rest_framework import generics


class SignUpView(generics.CreateAPIView):
    serializer_class = UserBaseSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)  # Defualt
        return Response(
            {"message": "ثبت نام موفق بود."}, status=status.HTTP_201_CREATED
        )


class LoginView(TokenObtainPairView):
    serializer_class = UserTokenObtainSerializer
