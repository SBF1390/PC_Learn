from django.urls import path
from . import views

urlpatterns = [
    # لیست و ایجاد بلاگ
    path("", views.BlogApiView.as_view()),
    path("<pk>/", views.BlogDetailApiView.as_view()),
    path("comments/", views.CommentGenericApiView.as_view()),
    path("<int:blog_pk>/comments/", views.CommentsOfBlogApiView.as_view()),
    path("category/", views.CategoryGenericApiView.as_view()),
    path("category/<pk>", views.CategoryDetailGenericApiView.as_view()),
]