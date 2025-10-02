from rest_framework import serializers
from .models import *

class courseserializersapiview(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
        
class sessionsserializersapiview(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
        
class DeleteCoursesApiveiw(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'
        
class CoursesApiview(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class sessionDeleteApiview(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class sessionApiview(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
