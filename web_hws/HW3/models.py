from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sq
import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('POSTGRES_USER')
password = os. getenv('POSTGRES_PASSWORD')
db = os.getenv('POSTGRES_DB')

engine = create_engine(f'postgresql://{user}:{password}@127.0.0.1:5431/{db}')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = 'owners'

    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    name = sq.Column(sq.String(50), nullable=False, unique=True)
    user_pass = sq.Column(sq.String(100), nullable=False, unique=True)


class Advertisement(Base):
    __tablename__ = 'advertisements'

    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    header = sq.Column(sq.Text, nullable=False)
    desc = sq.Column(sq.Text, nullable=True)
    created_at = sq.Column(sq.DateTime, server_default=sq.func.now())
    owner_id = sq.Column(sq.Integer, sq.ForeignKey('owners.id'), nullable=False)

    owner = relationship('User', backref='advertisements')


Base.metadata.create_all(engine)
