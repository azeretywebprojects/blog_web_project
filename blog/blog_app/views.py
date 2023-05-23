from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostCreateForm, PostEditForm, CategoryCreateForm
from .models import Post


def add_post(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('home')
    else:
        form = PostCreateForm()
    return render(request, 'add_post.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'article_list.html', {'post': post})


def index(request):
    if request.user.is_authenticated:
        posts = Post.objects.order_by('-created_at')
        return render(request, 'home.html', {'posts': posts})
    else:
        posts = []
    return render(request, 'home.html', {'posts': posts})


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostEditForm(instance=post)
    return render(request, 'update_post.html', {'form': form})


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'delete_post.html', {'post': post})


def add_category(request):
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryCreateForm()
    return render(request, 'add_category.html', {'form': form})


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})


# @login_required
# def add_comment(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         form = CommentCreateForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = CommentCreateForm()
#     return render(request, 'add_comment.html', {'form': form})

