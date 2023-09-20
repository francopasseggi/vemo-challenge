import pytest
from rest_framework.test import APIClient
from rest_framework import status
from .models import Todo


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_todo():
    todo = Todo.objects.create(
        title="Sample Todo", description="This is a sample description", completed=False
    )
    return todo


@pytest.mark.django_db
def test_todo_list(api_client):
    response = api_client.get("/api/v1/todos/")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_todo_create(api_client):
    data = {
        "title": "New Todo",
        "description": "This is a new todo",
        "completed": False,
    }
    response = api_client.post("/api/v1/todos/", data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Todo.objects.count() == 1
    assert Todo.objects.get().title == data["title"]


@pytest.mark.django_db
def test_todo_retrieve(api_client, create_todo):
    response = api_client.get(f"/api/v1/todos/{create_todo.id}/")
    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == create_todo.title


@pytest.mark.django_db
def test_todo_update(api_client, create_todo):
    data = {"title": "Updated Todo"}
    response = api_client.put(f"/api/v1/todos/{create_todo.id}/", data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert Todo.objects.get(id=create_todo.id).title == data["title"]


@pytest.mark.django_db
def test_todo_partial_update(api_client, create_todo):
    data = {"completed": True}
    response = api_client.patch(f"/api/v1/todos/{create_todo.id}/", data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert Todo.objects.get(id=create_todo.id).completed is True


@pytest.mark.django_db
def test_todo_delete(api_client, create_todo):
    response = api_client.delete(f"/api/v1/todos/{create_todo.id}/")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Todo.objects.count() == 0
