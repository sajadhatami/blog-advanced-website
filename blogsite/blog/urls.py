from django.urls import path
from . import views


# =========================================================
# Blog URLs Review Notes
# =========================================================

# 1. app_name = 'blog' is added → enables namespace and prevents name conflicts in large projects.
# 2. URL structure is clean and well-organized (post / author / feed separation).
# 3. Using slug in PostDetailView is standard and SEO-friendly.
# 4. Using ID for author detail is more stable and less ambiguous than slug.
# 5. Full CRUD is implemented for Post (create / update / delete / detail).
# 6. Feed endpoint should preferably be named as posts/feed/ or feed/posts/ for better consistency.
# 7. Naming consistency matters (post vs posts, author vs authors should be consistent across project).
# 8. URL order is correct (static routes come before dynamic routes).
# 9. Using app namespace improves reverse() and {% url %} safety in templates.
# 10. Overall structure is suitable for a personal blog and scalable to API or CMS in the future.

# =========================================================

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),


    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/delete/', views.PostDeleteView.as_view(), name='post_delete'),


    path('feed/', views.PostFeedView.as_view(), name='post_feed'),


    path('author/', views.AuthorListView.as_view(), name='author_list'),
    path('author/<int:id>/', views.AuthorDetailView.as_view(), name='author_detail'),
]