from django.urls import path, include
from . import views

urlpatterns = [
    # لیست و ایجاد بلاگ
    path('blog/', views.BlogGenericApiView.as_view(), name='blog-list'),
    path('blog/<int:pk>/', views.BlogDetailApiView.as_view(), name='blog-detail'),

    # لیست و ایجاد کامنت برای بلاگ مشخص
    path('blog/<int:blog_pk>/comments/', views.CommentGenericApiView.as_view(), name='blog-comments'),
]
