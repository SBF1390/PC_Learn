from django.urls import path
from .views import *

urlpatterns = [
    path('Courses/', CoursesListApiView.as_view()),
    path('session/', SessionsListApiView.as_view()),
    path('Courses/<int:pk>', CoursesDetailApiview.as_view()),
    path('session/<int:pk>', SessionDetailApiview.as_view()),
    path('Courses/<int:pk>/edit/', CourseUpdateApiView.as_view(), name='course-edit'),
    path('sessions/<int:pk>/edit/', SessionUpdateApiView.as_view(), name='session-edit'),
]
