from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response

class CoursesListApiView(generics.ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = courseserializersapiview
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']

class SessionsListApiView(generics.ListCreateAPIView):
    queryset = Session.objects.all()
    serializer_class = sessionsserializersapiview
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    
class DeleteCoursesApiview(generics.DestroyAPIView, generics.ListAPIView):
    serializer_class = DeleteCoursesApiveiw
    
    def get_queryset(self):
        Courses_id = self.kwargs['pk']
        return Courses.objects.filter(id=Courses_id)
    
class CoursesApiview(generics.ListAPIView):
    serializer_class = CoursesApiview
    
    def get_queryset(self):
        Courses_id = self.kwargs['pk']
        return Courses.objects.filter(id=Courses_id)
    
class sessionDeleteApiview(generics.DestroyAPIView, generics.ListAPIView):
    serializer_class = sessionDeleteApiview
    
    def get_queryset(self):
        session_id = self.kwargs['pk']
        return Courses.objects.filter(id=session_id)

class sessionApiview(generics.ListAPIView):
    serializer_class = sessionApiview
    
    def get_queryset(self):
        session_id = self.kwargs['pk']
        return  Courses.objects.filter(id=session_id)

class CourseUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'pk'
    
class SessionUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    lookup_field = 'pk'
