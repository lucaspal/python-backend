"""
Description: Tests for the library_app
"""

import os
import pytest

from library_app import app, db
from library_app.models import Author


# this fixture is run during initialization of every test function that uses it.
@pytest.fixture
def client():
    """
    Create a temporary db with some data in it for using in the tests.
    """
    app.config["TESTING"] = True
    app.testing = True

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

    client = app.test_client()
    with app.app_context():
        db.create_all()
        author1 = Author(name='Shakespeare', country='UK', year_of_birth=1800)
        author2 = Author(name='Stephen King', country='USA', year_of_birth=1945)
        db.session.add(author1)
        db.session.add(author2)
        db.session.commit()
    yield client
    os.remove('library_app/test.db')


def test_get_author_positive(client):
    response = client.get("/author/1")
    assert response.json == {"id": 1, "name": "Shakespeare", "country": "UK", "year_of_birth": 1800}


def test_get_author_missing(client):
    response = client.get("/author/3")
    assert response.json == {"response": "Author with id 3 not found"}


def test_get_authors_filter(client):
    response = client.get("/author?country=UK")
    assert response.json == {"data": [{"id": 1, "name": "Shakespeare", "country": "UK", "year_of_birth": 1800}]}


def test_create_author(client):
    response = client.post("/author", json={"name": "Test", "country": "DE", "year_of_birth": 2000})
    created_author = Author.query.filter_by(name="Test").first()
    assert created_author.name == "Test" and created_author.country == "DE" and created_author.year_of_birth == 2000
    assert response.status_code == 201
