from django.shortcuts import render
from django.shortcuts import render , redirect
from django.http import Http404
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets



class BlogGenericApiView(generics.ListCreateAPIView):
    queryset = Blog.objects.order_by('date').all()
    serializer_class = BlogSerializer


class BlogMixinDetailApiView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request, name, *args, **kwargs):
        blog = Blog.objects.get(name=name)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    
    def put(self, request: Request, pk):
        return self.update(request, pk)
    
    def delete(self, request:Request, pk):
        return self.destroy(request, pk)
