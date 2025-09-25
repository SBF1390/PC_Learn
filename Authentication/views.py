from django.shortcuts import render
from drf_spectacular.utils import extend_schema, inline_serializer, OpenApiResponse, OpenApiParameter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework import generics


class SignUpView(generics.CreateAPIView):
    queryset = UserBase.objects.all()
    serializer_class = UserSerializer