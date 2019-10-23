from django.contrib import admin
from django.urls import path
from . import views
from .views import PostDetailView, PostListView, PostCreateView

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post-create')
]
