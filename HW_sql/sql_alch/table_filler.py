from table_creator import Publisher, Book, Shop, Stock, Sale

def table_filler(session):
    publ_1 = Publisher(name='Пушкин')
    publ_2 = Publisher(name='Чехов')
    publ_3 = Publisher(name='Толстой')

    session.add(publ_1)
    session.add(publ_2)
    session.add(publ_3)
    session.commit()

    book_1 = Book(title='Капитанская дочь', id_publisher=1)
    book_2 = Book(title='Руслан и Людмида', id_publisher=1)
    book_3 = Book(title='Война и Мир', id_publisher=3)
    book_4 = Book(title='Вишневый сад', id_publisher=2)

    session.add(book_1)
    session.add(book_2)
    session.add(book_3)
    session.add(book_4)
    session.commit()

    shop_1 = Shop(name='Буквоед')
    shop_2 = Shop(name='Книги и Книжечки')

    session.add(shop_1)
    session.add(shop_2)

    session.commit()

    stock_1 = Stock(id_book=1, id_shop=1, count=1)
    stock_2 = Stock(id_book=2, id_shop=1, count=1)
    stock_3 = Stock(id_book=3, id_shop=2, count=1)
    stock_4 = Stock(id_book=4, id_shop=2, count=1)

    session.add(stock_1)
    session.add(stock_2)
    session.add(stock_3)
    session.add(stock_4)

    session.commit()

    sale_1 = Sale(price=300, date_sale='11.09.2021', id_stock=1, count=1)
    sale_2 = Sale(price=200, date_sale='11.09.2021', id_stock=2, count=1)
    sale_3 = Sale(price=100, date_sale='11.09.2021', id_stock=3, count=1)
    sale_4 = Sale(price=150, date_sale='11.09.2021', id_stock=4, count=1)

    session.add(sale_1)
    session.add(sale_2)
    session.add(sale_3)
    session.add(sale_4)

    session.commit()
