import pytest
from django.urls import reverse

from ..models import Post


@pytest.fixture
def test_add_post_view(client):
    url = reverse("add_post")
    response = client.get(url)

    assert response.status_code == 200

    data = {
        "title": "Test Post",
        "content": "This is a test post.",
    }

    response = client.post(url, data)
    assert response.status_code == 302

    assert Post.objects.filter(title="Test Post").exists()
