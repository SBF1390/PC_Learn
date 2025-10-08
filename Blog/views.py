from django.shortcuts import render
from django.shortcuts import render , redirect
from django.http import Http404
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Blog , Comment
from .serializers import BlogSerializer , CommentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets

# لیست و ایجاد بلاگ + فیلتر با query params
class BlogGenericApiView(generics.ListCreateAPIView):
    serializer_class = BlogSerializer 

    def get_queryset(self):
        queryset = Blog.objects.all()
        name = self.request.query_params.get('name')
        author = self.request.query_params.get('author')
        if name:
            queryset = queryset.filter(name__icontains=name)
        if author:
            queryset = queryset.filter(author__icontains=author)
        return queryset

# جزئیات بلاگ
class BlogDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# لیست و ایجاد کامنت
class CommentGenericApiView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        blog_id = self.kwargs['blog_pk']
        return Comment.objects.filter(blog_id=blog_id)

    def perform_create(self, serializer):
        blog_id = self.kwargs['blog_pk']
        serializer.save(blog_id=blog_id)

