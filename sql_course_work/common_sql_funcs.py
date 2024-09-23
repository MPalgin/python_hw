from table_creator import create_tables, table_filler
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from table_creator import Translate, WordDict, WorldVariables, User


def table_scema_creator():
    DSN = "postgresql://postgres:admin@localhost:5432/netology_db"
    engine = sqlalchemy.create_engine(DSN)
    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    table_filler(session)
    return session


def get_common_words(session, word_type, uid):
    if word_type == 'common':
        query = (session.query(WordDict.word_id, WordDict.word, Translate.name).join(Translate).
                 filter(sqlalchemy.or_(WordDict.user_id == sqlalchemy.sql.null(), WordDict.user_id == uid)).all())
    else:
        query = session.query(WorldVariables.name).all()
    return query


def delete_word_from_user_db(session, word, uid):
    query = session.query(WordDict.word_id, User.user_id).join(WordDict).join(Translate)

    if query.filter(WordDict.word == word).filter(User.user_id == uid).all():
        word_id = query.filter(WordDict.word == word).filter(User.user_id == uid).all()[0][0]
        translate_word_data = session.query(Translate).filter(Translate.word_id == word_id).first()
        session.delete(translate_word_data)
        word_data = session.query(WordDict).filter(WordDict.word_id == word_id).first()
        session.delete(word_data)
        session.commit()
        return True
    return False


def add_new_user_word(session, word: dict, uid):
    query = session.query(WordDict.word_id, User.user_id).join(User)
    if not query.filter(WordDict.word == word['new_word']).filter(User.user_id == uid).all():
        session.add(WordDict(user_id=uid, word=word['new_word']))
        session.commit()
        query = session.query(WordDict.word_id, User.user_id).join(User)
        word_id = query.filter(WordDict.word == word['new_word']).filter(User.user_id == uid).all()[0][0]
        session.add(Translate(word_id=word_id, name=word['translate']))
        session.commit()
        return True
    return False


def add_user_id(session, uid):
    session.add(User(user_id=uid))
    session.commit()