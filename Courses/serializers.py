from rest_framework import serializers
from .models import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = "__all__"


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"