from django.urls import path

from .views import add_category, add_post, delete_post, edit_post, home, like_post, post_detail

urlpatterns = [
    path("", home, name="home"),
    path("post/<int:pk>/", post_detail, name="post_detail"),
    path("post/add/", add_post, name="add_post"),
    path("post/<int:pk>/edit/", edit_post, name="edit_post"),
    path("post/<int:pk>/delete/", delete_post, name="delete_post"),
    path("category/add/", add_category, name="add_category"),
    path("like_post/<int:post_id>/<str:action>/", like_post, name="like_post"),
]
