import pytest

# from test_view import test_add_post_view


@pytest.mark.run(order=1)
def test_view(test_add_post_view):
    assert True
