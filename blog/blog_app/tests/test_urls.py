import pytest
from django.urls import reverse


@pytest.fixture
def client():
    from django.test import Client

    return Client()


@pytest.mark.django_db
def test_home_url_resolves(client):
    url = reverse("home")
    assert url == "/"


@pytest.mark.django_db
def test_post_detail_url_resolves(client):
    url = reverse("post_detail", args=[1])
    assert url == "/post/1/"


@pytest.mark.django_db
def test_add_post_url_resolves(client):
    url = reverse("add_post")
    assert url == "/post/add/"


@pytest.mark.django_db
def test_edit_post_url_resolves(client):
    url = reverse("edit_post", args=[1])
    assert url == "/post/1/edit/"


@pytest.mark.django_db
def test_delete_post_url_resolves(client):
    url = reverse("delete_post", args=[1])
    assert url == "/post/1/delete/"
