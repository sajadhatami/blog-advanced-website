from django.core.checks import Tags
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView , CreateView , UpdateView , DeleteView
from .models import Post
from .models import Category, Tag




# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status=True).order_by('-created_at')

class PostDetailView(DetailView):
    pass

class PostCreateView(CreateView):
    pass

class PostUpdateView(UpdateView):
    pass

class PostDeleteView(DeleteView):
    pass

class PostFeedView(ListView):
    pass

class AuthorListView(ListView):
    pass

class AuthorDetailView(DetailView):
    pass

