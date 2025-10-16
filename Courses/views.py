from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import filters

class CoursesListApiView(generics.ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']

class SessionsListApiView(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']

class CoursesDetailApiview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Courses.objects.all()

class SessionDetailApiview(generics.ListAPIView):
    serializer_class = SessionSerializer
    queryset = Session.objects.all()

class CourseUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'pk'
    
class SessionUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    lookup_field = 'pk'
