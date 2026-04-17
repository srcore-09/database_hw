from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


book_genre_table = Table('book_genre_table', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('genre_id', Integer, ForeignKey('genres.id'))
)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    passport = relationship("Passport", back_populates="user", uselist=False)

class Passport(Base):
    __tablename__ = 'passports'
    id = Column(Integer, primary_key=True)
    number = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="passport")


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", back_populates="books")
    # 3. Связь N:N
    genres = relationship("Genre", secondary=book_genre_table, back_populates="books")

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", secondary=book_genre_table, back_populates="genres")


engine = create_engine('sqlite:///my_library.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()




new_author = Author(name="Chingiz Aitmatov")
b1 = Book(title="Plakha", author=new_author)
g1 = Genre(name="Classic")
b1.genres.append(g1)

session.add(new_author)
session.commit()


find_book = session.query(Book).filter_by(title="Plakha").first()
print(f"Книга: {find_book.title}")


find_book.title = "The White Ship"
session.commit()



print("Готово! База создана и данные проверены.")