from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from .models import *


class UserBaseSerializer(ModelSerializer):
    role = serializers.SlugRelatedField(
        slug_field="name", queryset=Role.objects.all(), required=False
    )

    class Meta:
        model = UserBase
        fields = ["UserName", "FName", "LName", "password", "role"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        role = validated_data.pop("role", None)
        password = validated_data.pop("password")
        user = UserBase(**validated_data)
        if role:
            user.role = role
        user.set_password(password)
        user.save()
        return user

    def validate_UserName(self, value):
        if " " in value:
            raise serializers.ValidationError(
                "نمک در نمکدان شوری ندارد,فاصله در نام کاربری جایی ندارد."
            )
        return value

    def validate_password(self, value):
        user = UserBase(
            UserName=self.initial_data.get("UserName"),
            FName=self.initial_data.get("FName"),
            LName=self.initial_data.get("LName"),
        )
        try:
            validate_password(password=value, user=user)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value


class UserTokenObtainSerializer(TokenObtainPairSerializer):
    username_field = "UserName"