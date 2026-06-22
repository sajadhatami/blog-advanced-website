from django.contrib.auth import get_user_model
from django.core.checks import Tags
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView , CreateView , UpdateView , DeleteView
from .models import Post
from .models import Category, Tag

User = get_user_model()


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(status=True).order_by('-created_at')

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

class PostCreateView(CreateView):
    model = Post
    fields = ["title",
        "author",
        "excerpt",
        "content",
        "image",
        "category",
        "tags",
        "status",
        "allow_comments",
        "is_featured",
        "meta_title",
        "meta_description",
              ]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy('blog:post_list')

class PostUpdateView(UpdateView):
    model = Post
    fields = PostCreateView.fields
    template_name = "blog/post_form.html"
    success_url = reverse_lazy('blog:post_list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("blog:post_list")

class PostFeedView(ListView):
    model = Post
    template_name = "blog/feed.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(
            status=True,
            is_featured=True
        ).order_by('-created_at')

class AuthorListView(ListView):
    model = User
    template_name = 'blog/author_list.html'
    context_object_name = 'authors'

class AuthorDetailView(DetailView):
    model = Post
    template_name = "blog/author_detail.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.filter(author__id=self.kwargs["id"])
