from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# Through engine SQLAlchemy communicates with your database
engine = create_engine('sqlite:///funny.sqlite', echo=False)

# ORM needs a session to talk to your tables and make queries. As session sets the middle ground between
# python objects and database

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Lets start creating tables


class Product(Base):
    __tablename__ = 'products'  # This is the table name inside the db

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    products = relationship(Product, backref="users")

    def __repr__(self):
        return f'User {self.name}'


# We need base class and engine to actually create the tables
Base.metadata.create_all(engine)

# When want to add only one tables, other tables are already there in the db
# Product.__table__.create(engine)


# Inserting records
user = User(name='Luca', password='totally_secure_pw')
session.add(user)
session.commit()

# Retrieving records
all_luca = session.query(User).filter_by(name='Luca').all()  # return all records
count_query = session.query(User).filter_by(name='Luca').count()  # counts the records
first_luca = session.query(User).filter_by(name='Luca').first()  # returns the first record

print("first record in user table", first_luca.id)

something_like_luca = session.query(User).filter(User.name.like('%uc%')).first()
print("filter query in user table:", something_like_luca)

user = User(name='Jai')
product = Product(name='ipad', user=user)

session.add_all([user, product])
session.commit()

query = session.query(Product).filter_by(user_id=2).first()
print("query from product table (product name):", query.name)
print("query from product table (related users):", query.users)
