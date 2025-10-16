from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import generics
from django.template import loader
from rest_framework import status
from .permissions import *
from .serializers import *
from .models import *


@extend_schema(
    tags=["Auth"],
    summary="ثبت‌نام کاربر جدید",
    description="ایجاد حساب کاربری جدید با اطلاعات کاربر.",
    request={
        "application/json": {
            "example": {
                "UserName": "reza123",
                "FName": "رضا",
                "LName": "اکبری",
                "password": "RezaStrongPass123!",
            }
        }
    },
    responses={
        201: OpenApiResponse(
            response={
                "application/json": {"example": {"message": "ثبت نام موفق بود."}}
            },
            description="ثبت‌نام موفق",
        ),
        400: OpenApiResponse(description="ورودی نامعتبر"),
    },
)
class SignUpView(generics.CreateAPIView):
    serializer_class = UserBaseSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        role_name = request.data.get("role", "member")
        role = Role.objects.filter(name=role_name).first()
        serializer.save(role=role)
        return Response(
            {"message": "ثبت نام موفق بود."}, status=status.HTTP_201_CREATED
        )


@extend_schema(
    tags=["Auth"],
    summary="ورود با JWT",
    description="دریافت توکن دسترسی و رفرش از طریق نام کاربری و رمز عبور.",
    request={
        "application/json": {
            "example": {"UserName": "reza123", "password": "RezaStrongPass123!"}
        }
    },
    responses={
        200: OpenApiResponse(
            response={
                "application/json": {
                    "example": {"refresh": "توکن رفرش...", "access": "توکن دسترسی..."}
                }
            },
            description="ورود موفق",
        ),
        401: OpenApiResponse(description="نام کاربری یا رمز عبور اشتباه است"),
    },
)
class LoginView(TokenObtainPairView):
    serializer_class = UserTokenObtainSerializer


@extend_schema(
    tags=["Auth"],
    summary="خروج کاربر",
    description="ابطال توکن رفرش و خروج کاربر از سیستم.",
    request={"application/json": {"example": {"refresh": "توکن رفرش"}}},
    responses={
        200: OpenApiResponse(
            response={
                "application/json": {"example": {"message": "خروج موفقیت آمیز بود."}}
            },
            description="خروج موفق",
        ),
        401: OpenApiResponse(description="توکن معتبر نیست یا ارسال نشده است"),
    },
)
class LogOutView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
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