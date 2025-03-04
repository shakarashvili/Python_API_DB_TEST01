import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com/posts"  # Example API


@pytest.fixture
def sample_post_data():
    return {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }


def test_get_request():
    """Test GET request to fetch posts"""
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure response is a list of posts


def test_post_request(sample_post_data):
    """Test POST request to create a new post"""
    response = requests.post(BASE_URL, json=sample_post_data)
    assert response.status_code == 201  # 201 Created
    response_json = response.json()
    assert response_json["title"] == sample_post_data["title"]
    assert response_json["body"] == sample_post_data["body"]
    assert response_json["userId"] == sample_post_data["userId"]


def test_put_request(sample_post_data):
    """Test PUT request to update a post"""
    updated_data = sample_post_data.copy()
    updated_data["title"] = "updated title"

    post_id = 1  # Assume we update post with ID 1
    response = requests.put(f"{BASE_URL}/{post_id}", json=updated_data)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["title"] == "updated title"


def test_delete_request():
    """Test DELETE request to remove a post"""
    post_id = 1  # Assume we delete post with ID 1
    response = requests.delete(f"{BASE_URL}/{post_id}")
    assert response.status_code == 200  # JSONPlaceholder returns 200, but real APIs may return 204
