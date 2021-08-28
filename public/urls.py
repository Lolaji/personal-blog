from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('post/<str:username>/', UserPostListView.as_view(), name="user-posts"),
    path('post/new/', PostCreateView.as_view(), name="blog-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="blog-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="blog-delete"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="blog-detail")
]