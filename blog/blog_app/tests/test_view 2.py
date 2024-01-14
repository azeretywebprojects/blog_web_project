# import pytest
# from django.contrib.auth.models import User
# from django.test import Client
# from django.urls import reverse
# from mixer.backend.django import mixer
#
#
# @pytest.fixture
# def client():
#     return Client()
#
#
# @pytest.fixture
# def user():
#     return mixer.blend(User)
#
#
# @pytest.mark.django_db
# def test_add_post_view(client, user):
#     client.force_login(user)
#
#     response = client.post(
#         reverse("add_post"),
#         data={
#             "title": "Test Post",
#             "content": "This is a test post content",
#         },
#     )
#
#     assert response.status_code == 302
#
#     assert response.url == reverse("home")
#
#
# @pytest.mark.django_db
# def test_edit_post_view(client, user):
#     post = mixer.blend("blog_app.Post", author=user)
#
#     client.force_login(user)
#
#     response = client.post(
#         reverse("edit_post", args=[post.pk]),
#         data={
#             "title": "Edited Test Post",
#             "content": "This is an edited test post content",
#         },
#     )
#
#     assert response.status_code == 302
#
#     assert response.url == reverse("post_detail", args=[post.pk])
#
#
# @pytest.mark.django_db
# def test_delete_post_view(client, user):
#     post = mixer.blend("blog_app.Post", author=user)
#
#     client.force_login(user)
#
#     response = client.post(reverse("delete_post", args=[post.pk]))
#
#     assert response.status_code == 302
#
#     assert response.url == reverse("home")
