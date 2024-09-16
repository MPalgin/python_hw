from table_creator import Book, Shop, Sale, Publisher, Stock, create_tables
from table_filler import table_filler
import sqlalchemy
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    DSN = "postgresql://postgres:admin@localhost:5432/netology_db"
    engine = sqlalchemy.create_engine(DSN)
    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    table_filler(session)

    writer = input('Input writer name or id ')
    query = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale)
    if writer.isdigit():
        query = query.filter(Publisher.id == writer).all()
    else:
        query = query.filter(Publisher.name == writer).all()

    for title, name, price, date_sale in query:
        print(f"{title:<40} | {name:<10} | {price:<8} | {date_sale}")

    session.commit()
