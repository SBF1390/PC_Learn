from django.urls import path, include
from . import views

urlpatterns = [
    path('blog/' , views.BlogGenericApiView.as_view()),
    path('blog/<str:name>/' , views.BlogMixinDetailApiView.as_view()),
    path('blog/<str:name>/<str:author>/' , views.BlogMixinDetailApiView.as_view()),
]