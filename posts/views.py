from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic import (
    ListView,
    DetailView,
    # CreateView,
    # UpdateView,
    # DeleteView
)
from .models import Post, Comment, UnloggedComment


def posts(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/posts.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'posts/posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-created_at']
    # paginate_by = 5



class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/article.html'


# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['title', 'content']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


# class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Post
#     fields = ['title', 'content']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False


# class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Post
#     success_url = '/'

#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False


# def about(request):
#     return render(request, 'blog/about.html', {'title': 'About'})

# Save answer comment
def save_comment(request):
     if request.method=='POST':
          content = request.POST['content']
          postid = request.POST['postid']
          post = Post.objects.get(pk=postid)
          created_by = request.user
          Comment.objects.create(
               post=post,
               content=content,
               created_by=created_by
          )
          return JsonResponse({'bool':True})

# Save answer comment
def save_unlogged_comment(request):
     if request.method=='POST':
          content = request.POST['content']
          postid = request.POST['postid']
          post = Post.objects.get(pk=postid)
          name = request.POST['name']
          email = request.POST['email']
          UnloggedComment.objects.create(
               post=post,
               content=content,
               name = name,
               email = email
          )
          return JsonResponse({'bool':True}) 