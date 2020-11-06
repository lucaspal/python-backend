"""
Description: Functions related to Author
"""
from library_app import db
from library_app.models import Author


def get_all(filters):
    allowed_filters = ['name', 'country', 'year_of_birth']
    final_filters = {k: v for k, v in filters.items() if k in allowed_filters}
    authors = Author.query.filter_by(**final_filters).all()
    return authors


def get(author_id):
    return Author.query.filter_by(id=author_id).first()


def create(name, country=None, year_of_birth=None):
    new_author = Author(name=name, country=country, year_of_birth=year_of_birth)
    db.session.add(new_author)
    db.session.commit()


def update(author_id, fields):
    result = Author.query.filter_by(id=author_id).update(fields)
    db.session.commit()
    return result


def delete(author):
    db.session.delete(author)
    db.session.commit()
