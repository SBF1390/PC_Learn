from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer
from .models import *


class UserBaseSerializer(ModelSerializer):
    class Meta:
        model = UserBase
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = UserBase(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserTokenObtainSerializer(TokenObtainPairSerializer):
    username_field = "UserName"