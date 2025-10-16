from django.shortcuts import render, redirect
from django.http import Http404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics
from drf_spectacular.utils import extend_schema, OpenApiExample
from .models import *
from .serializers import *

# ---------------------------
# Blog Views
# ---------------------------


@extend_schema(
    summary="List or Create Blogs",
    description=(
        "این API لیست تمام بلاگ‌ها را برمی‌گرداند. "
        "همچنین می‌توانید با ارسال داده صحیح، یک بلاگ جدید ایجاد کنید. "
        "فیلدهای مورد نیاز برای ایجاد بلاگ شامل name, author, content, tags و category هستند."
    ),
    tags=["Blogs"],
    examples=[
        OpenApiExample(
            "نمونه بلاگ",
            value={
                "name": "آموزش Django",
                "author": "Ali",
                "content": {"text": "این یک بلاگ نمونه است"},
                "tags": "django,rest",
                "category": [1, 2],
            },
            request_only=True,
        ),
    ],
    operation_id="list_or_create_blog",
)
class BlogApiView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


@extend_schema(
    summary="Retrieve, Update, or Delete a Blog",
    description=(
        "این API جزئیات یک بلاگ مشخص را برمی‌گرداند، "
        "می‌تواند آن را بروزرسانی کند یا حذف نماید. "
        "شناسه بلاگ از طریق path parameter `pk` ارسال می‌شود."
    ),
    tags=["Blogs"],
    operation_id="blog_detail",
)
class BlogDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# ---------------------------
# Comment Views
# ---------------------------


@extend_schema(
    summary="List or Create Comments",
    description=(
        "این API لیست تمام کامنت‌ها را برمی‌گرداند یا کامنت جدید ایجاد می‌کند. "
        "برای ایجاد کامنت نیاز به blog (id بلاگ)، author و text دارید."
    ),
    tags=["Comments"],
    examples=[
        OpenApiExample(
            "نمونه کامنت",
            value={"blog": 1, "author": "Sara", "text": "ممنون بابت مقاله!"},
            request_only=True,
        ),
    ],
    operation_id="list_or_create_comment",
)
class CommentGenericApiView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


@extend_schema(
    summary="List Comments of a Specific Blog",
    description=(
        "این API تمام کامنت‌های مربوط به یک بلاگ مشخص را برمی‌گرداند. "
        "شناسه بلاگ از طریق path parameter `blog_pk` ارسال می‌شود."
    ),
    tags=["Comments"],
    operation_id="comments_of_blog",
)
class CommentsOfBlogApiView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        blog_id = self.kwargs["blog_pk"]
        return Comment.objects.filter(blog_id=blog_id)


# ---------------------------
# Category Views
# ---------------------------


@extend_schema(
    summary="List or Create Categories",
    description=(
        "این API لیست تمام دسته‌بندی‌ها را برمی‌گرداند یا دسته‌بندی جدید ایجاد می‌کند. "
        "برای ایجاد دسته‌بندی نیاز به نام دسته‌بندی دارید."
    ),
    tags=["Categories"],
    examples=[
        OpenApiExample(
            "نمونه دسته‌بندی", value={"name": "Programming"}, request_only=True
        ),
    ],
    operation_id="list_or_create_category",
)
class CategoryGenericApiView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


@extend_schema(
    summary="Retrieve, Update, or Delete a Category",
    description=(
        "این API جزئیات یک دسته‌بندی مشخص را برمی‌گرداند، "
        "می‌تواند آن را بروزرسانی کند یا حذف نماید. "
        "شناسه دسته‌بندی از طریق path parameter `pk` ارسال می‌شود."
    ),
    tags=["Categories"],
    operation_id="category_detail",
)
class CategoryDetailGenericApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer