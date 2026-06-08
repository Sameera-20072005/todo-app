"""Tests for todo-app."""
import pytest
from src.main import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
