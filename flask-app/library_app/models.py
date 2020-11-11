"""
Description: Models: Classes representing DB tables.
"""
from library_app import db

from sqlalchemy.inspection import inspect as inspect


class Serializer(object):
    """Class for serializing SQLAlchemy objects into dicts."""

    @staticmethod
    def is_primitive(obj):
        return type(obj) in (int, float, str, bool)

    def serialize(self):
        fields = inspect(self).attrs.keys()
        return {c: getattr(self, c) for c in fields if Serializer.is_primitive(getattr(self, c))}

    @staticmethod
    def serialize_list(list_obj):
        return [m.serialize() for m in list_obj]


class Author(db.Model, Serializer):
    # See http://flask-sqlalchemy.pocoo.org/2.0/models/#simple-example
    # for details on the column types.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(80))
    year_of_birth = db.Column(db.Integer)
    books = db.relationship("Book", backref="author", lazy=True)

    def __repr__(self):
        return f'Author name:{self.name} country:{self.country} year: {self.year_of_birth}'


class Book(db.Model, Serializer):
    # See http://flask-sqlalchemy.pocoo.org/2.0/models/#simple-example
    # for details on the column types.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))


    def __repr__(self):
        return f'Book title:{self.name} author: {self.author.name}'


if __name__ == '__main__':
    db.create_all()
    db.session.commit()
