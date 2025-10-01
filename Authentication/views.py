from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import generics
from django.template import loader
from rest_framework import status
from .serializers import *
from .models import *


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


class LogOutView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            return Response(
                {"message": "خروج موفقیت امیز بود."},
                status=status.HTTP_205_RESET_CONTENT,
            )
        except Exception as e:
            return Response(
                {"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST
            )

def Doc(request):
    Template = loader.get_template("Docs/index.html")
    return HttpResponse(Template.render())