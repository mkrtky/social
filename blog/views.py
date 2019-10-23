from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView, ListView

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['date_posted']
