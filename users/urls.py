from django.urls import path
from . import views
from .views import PostList

urlpatterns = [
    # path('dashboard/', views.dashboard, name='dashboard'),
    path('post_list/', PostList.as_view(), name='post-list')
]