import psycopg2


def create_db(db_connection):
    with db_connection.cursor() as db_cur:
        db_cur.execute("CREATE TABLE IF NOT EXISTS clients_table("
                       "client_id SERIAL PRIMARY KEY NOT NULL UNIQUE,"
                       "client_name VARCHAR(40) NOT NULL UNIQUE,"
                       "client_surname VARCHAR(60) NOT NULL UNIQUE,"
                       "client_email VARCHAR(100) NOT NULL UNIQUE);")

        db_cur.execute("CREATE TABLE IF NOT EXISTS phones_numbers("
                       "phone_id SERIAL PRIMARY KEY,"
                       "client_id INTEGER REFERENCES clients_table(client_id),"
                       "phone VARCHAR(12));")


def add_clients(db_connection, client_info: dict):
    with db_connection.cursor() as db_cur:
        db_cur.execute('INSERT INTO clients_table (client_name, client_surname, client_email)'
                       'VALUES(%s, %s, %s)'
                       'RETURNING client_id, client_name, client_surname, client_email;',
                       (client_info['client_name'], client_info['client_surname'], client_info['client_email']))
        return db_cur.fetchone()


def add_phones(db_connection, client_info: dict):
    with db_connection.cursor() as db_cur:
        db_cur.execute('INSERT INTO phones_numbers (client_id, phone)'
                       'VALUES(%s, %s)'
                       'RETURNING client_id, phone;',
                       (client_info['client_id'], client_info['phone']))
        return db_cur.fetchone()


def update_client_info(db_connection, client_id, client_info: dict):
    with db_connection.cursor() as db_cur:
        db_cur.execute('UPDATE clients_table SET client_name=%s, client_surname=%s, client_email=%s'
                       'WHERE client_id=%s;', (client_info['client_name'], client_info['client_surname'],
                                               client_info['client_email'], str(client_id)))
        db_cur.execute('SELECT * FROM clients_table WHERE client_id=%s;', str(client_id))

        if 'phone' in client_info:
            db_cur.execute('UPDATE phones_numbers SET phone=%s WHERE client_id=%s;', (client_info['phone'],
                           str(client_id)))
            db_cur.execute('SELECT * FROM clients_table c LEFT JOIN phones_numbers p ON c.client_id = p.client_id '
                           'WHERE c.client_id=%s;', str(client_id))

        return db_cur.fetchall()


def delete_phone(db_connection, client_id):
    with db_connection.cursor() as db_cur:
        db_cur.execute('DELETE FROM phones_numbers WHERE client_id=%s RETURNING client_id;', str(client_id))
        return db_cur.fetchone()


def delete_client(db_connection, client_id):
    delete_phone(db_connection, client_id)
    with db_connection.cursor() as db_cur:
        db_cur.execute('DELETE FROM clients_table WHERE client_id=%s RETURNING client_id;', str(client_id))
        return db_cur.fetchone()


def find_client_info(db_connection, client_info: dict):
    for data in ['client_name', 'client_surname', 'client_email', 'phone']:
        if data not in client_info:
            client_info[data] = None
    with db_connection.cursor() as db_cur:
        db_cur.execute('SELECT * FROM clients_table c '
                       'LEFT JOIN phones_numbers p ON c.client_id = p.client_id '
                       'WHERE (client_name = %(client_name)s OR %(client_name)s IS NULL) '
                       'AND (client_surname = %(client_surname)s OR %(client_surname)s IS NULL) '
                       'AND (client_email = %(client_email)s OR %(client_email)s IS NULL) '
                       'AND (phone = %(phone)s OR %(phone)s IS NULL);'
                       , {'client_name': client_info['client_name'], 'client_surname': client_info['client_surname'],
                          'client_email': client_info['client_email'], 'phone': client_info['phone']})
        return db_cur.fetchall()


if __name__ == '__main__':
    with psycopg2.connect(database='netology_db', user='postgres', password='admin') as db_connection:
        create_db(db_connection)
        for client_name, client_surname, client_email in zip(['Andrey', 'Bob', 'Vasia'], ['Perviy', 'Gerasimov',
                                                                                          'Ivanov'], ['Andrey@mail.ru',
                                                                                                      'Bob@gmail.com',
                                                                                                      'Vasia@mail.ru']):
            print(add_clients(db_connection, {'client_name': client_name, 'client_surname': client_surname,
                                              'client_email': client_email}))
        for client_id, phone in zip([1, 2, 3], [89210000001, 89210000002, 89210000003]):
            print(add_phones(db_connection, {'client_id': client_id, 'phone': phone}))

        print(update_client_info(db_connection, 2, {'client_name': 'Marta',
                                                    'client_surname': 'Vasileva', 'client_email': 'Marta@yandex.ru',
                                                    'phone': '11111111111'}))
        print(find_client_info(db_connection, {'client_name': 'Marta'}))

        print(delete_phone(db_connection, 1))
        print(delete_client(db_connection, 1))
