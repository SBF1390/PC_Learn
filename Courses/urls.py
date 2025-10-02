from django.urls import path
from .views import *

urlpatterns = [
    path('Courses/', CoursesListApiView.as_view()),
    path('session/', SessionsListApiView.as_view()),
    path('Courses/<int:pk>/Delete/', DeleteCoursesApiview.as_view()),
    path('Courses/<int:pk>', CoursesApiview.as_view()),
    path('session/<int:pk>/Delete/', sessionDeleteApiview.as_view()),
    path('session/<int:pk>', sessionApiview.as_view()),
    path('Courses/<int:pk>/edit/', CourseUpdateApiView.as_view(), name='course-edit'),
    path('sessions/<int:pk>/edit/', SessionUpdateApiView.as_view(), name='session-edit'),
]
