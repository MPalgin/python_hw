import sqlalchemy as sq
from sqlalchemy import cast
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import sqlalchemy

Base = declarative_base()


class User(Base):
    __tablename__ = "userdata"
    user_id = sq.Column(sq.Integer, primary_key=True)

class WordDict(Base):
    __tablename__ = "word_dict"
    word_id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, sq.ForeignKey('userdata.user_id'), nullable=True)
    word = sq.Column(sq.String(length=40), unique=True)

    user = relationship(User, backref='user_words')


class Translate(Base):
    __tablename__ = "translate"
    id = sq.Column(sq.Integer, primary_key=True)
    word_id = sq.Column(sq.Integer, sq.ForeignKey('word_dict.word_id'), nullable=False)
    name = sq.Column(sq.String(length=40), unique=True)

    word = relationship(WordDict, backref='translates')


class WorldVariables(Base):
    __tablename__ = "randomwords"
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)


def create_tables(engine):
    Base.metadata.create_all(engine)


def table_filler(session):
    words = {'Мир': 'World', 'Дом': 'Home', 'Кот': 'Cat', 'Твой': 'Your', 'Мой': 'My', 'Спина': 'Back', 'Легко': 'Easy', 'Рыба': 'Fish', 'Счастье': 'Happiness'}
    word_num = 1
    for word, translate in words.items():
        session.add(WordDict(word=word))
        session.add(Translate(word_id=word_num, name=translate))
        word_num += 1
    session.commit()

    random_words = ['Happy', 'Education', 'It', 'They', 'House', 'Learn', 'Tolk', 'She', 'Back', 'Hard', 'Boy', 'Girl',
                    'Brother', 'Father', 'Shark', 'Bar', 'Air', 'Car', 'Dog']
    for word in random_words:
        session.add(WorldVariables(name=word))
    session.commit()
