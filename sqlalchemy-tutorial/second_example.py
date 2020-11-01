from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///imagedb.sqlite', echo=True)

Base = declarative_base()

tags = Table('tag_image', Base.metadata,
             Column('tag_id', Integer, ForeignKey('tags.id')),
             Column('image_id', Integer, ForeignKey('images.id'))
             )


class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), unique=True, nullable=False)
    likes = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    tags = relationship('Tag', secondary=tags,
                        backref=backref('images', lazy='dynamic'))
    comments = relationship('Comment', cascade="all,delete", backref='image', lazy='dynamic')

    def __repr__(self):
        str_created_at = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return "<Image (uuid='%s', likes='%d', created_at=%s)>" % (self.uuid, self.likes, str_created_at)


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)

    def __repr__(self):
        return "<Tag (name='%s')>" % self.name


class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    text = Column(String(2000))
    image_id = Column(Integer, ForeignKey('images.id'))

    def __repr__(self):
        return "<Comment (text='%s')>" % self.text


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Insert the data

tag_good = Tag(name='SQL')
tag_better = Tag(name='Sqlite3')
tag_best = Tag(name='SQLAlchemy')

comment_rhino = Comment(text='Interesting! Now I am not using SQL while talking to database')

image_car = Image(uuid='uuid_auto',
                  tags=[tag_good, tag_better],
                  created_at=(datetime.utcnow() - timedelta(days=1)))

image_another_car = Image(uuid='uuid_another_auto',
                          tags=[tag_good])

image_rhino = Image(uuid='uuid_rhino',
                    tags=[tag_best],
                    comments=[comment_rhino])

session.add_all([tag_good, tag_better, tag_better, comment_rhino, image_car, image_another_car, image_rhino])
session.commit()

# Update
image_to_update = session.query(Image).filter(Image.uuid == 'uuid_rhino').first()
# Increase the number of upvotes:
image_to_update.likes = image_to_update.likes + 1
# And commit the work:
session.commit()

# Delete
session.delete(image_rhino)
