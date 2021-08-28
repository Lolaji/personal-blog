from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from public.models import Post

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'public/pages/home.html', context)

class PostCreateView (LoginRequiredMixin, CreateView):
    model=Post
    template_name = 'public/pages/Post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView (LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Post
    template_name = 'public/pages/Post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView (LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Post
    success_url='/'
    template_name = 'public/pages/delete_post.html'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostListView (ListView):
    model = Post
    template_name = 'public/pages/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2


class UserPostListView (ListView):
    model = Post
    template_name = 'public/pages/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView (DetailView):
    model = Post
    template_name = 'public/pages/detail.html'