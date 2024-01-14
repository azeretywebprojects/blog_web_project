from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoryCreateForm, PostForm
from .models import Like, Post


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PostForm()
    return render(request, "add_post.html", {"form": form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "article_list.html", {"post": post})


def index(request):
    if request.user.is_authenticated:
        posts = Post.objects.order_by("-created_at")
        return render(request, "home.html", {"posts": posts})
    else:
        posts = []
    return render(request, "home.html", {"posts": posts})


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "update_post.html", {"form": form})


def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("home")
    return render(request, "delete_post.html", {"post": post})


def add_category(request):
    if request.method == "POST":
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CategoryCreateForm()
    return render(request, "add_category.html", {"form": form})


def home(request):
    posts = Post.objects.all()
    return render(request, "home.html", {"posts": posts})


def like_post(request, post_id, action):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if action == "like":
        Like.objects.create(user=user, post=post, like_status=True)
        post.like += 1
    elif action == "dislike":
        Like.objects.create(user=user, post=post, like_status=False)
        post.dislike += 1

    post.save()

    data = {"like": post.like, "dislike": post.dislike}
    return JsonResponse(data)


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
