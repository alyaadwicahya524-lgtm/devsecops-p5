import pytest

from app import create_app
from utils import clean_title, validate_title


@pytest.fixture
def client():
    return create_app().test_client()


def test_validate_title():
    assert validate_title("Belajar DevSecOps")
    assert not validate_title("   ")
    assert not validate_title(123)
    assert not validate_title("a" * 101)


def test_clean_title():
    assert clean_title("  halo  ") == "halo"


def test_create_task(client):
    res = client.post("/tasks", json={"title": "Tugas 1"})
    assert res.status_code == 201
    assert res.get_json()["title"] == "Tugas 1"


def test_create_task_invalid(client):
    res = client.post("/tasks", json={"title": ""})
    assert res.status_code == 400


def test_mark_done_and_delete(client):
    task_id = client.post("/tasks", json={"title": "Tugas 2"}).get_json()["id"]

    res = client.put(f"/tasks/{task_id}/done")
    assert res.get_json()["done"] is True

    assert client.delete(f"/tasks/{task_id}").status_code == 200
    assert client.delete(f"/tasks/{task_id}").status_code == 404