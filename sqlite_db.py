import sqlite3


def create_table():
    print('Created Table')
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    create_table_store = 'CREATE TABLE IF NOT EXISTS store(id int primary key, store_name text,store_location text)'
    create_table_user = 'CREATE TABLE IF NOT EXISTS user(id int primary key, username text,password text)'
    cursor.execute(create_table_store)
    cursor.execute(create_table_user)

    connection.close()


def insert_user():
   User1 = (1,'shakib','12345')
   User2 = (2, 'shojon', '12345')

   connection = sqlite3.connect('data.db')
   cursor = connection.cursor()

   insert_dummy_store = 'INSERT INTO user (id , username, password) VALUES (?,?,?)'
   cursor.execute(insert_dummy_store , User1)
   cursor.execute(insert_dummy_store , User2)

   connection.commit()

   connection.close()


def insert_store():
   Store1 = (1,'Book','12345')
   Store2 = (2, 'Fish', '12345')

   connection = sqlite3.connect('data.db')
   cursor = connection.cursor()

   insert_dummy_store = 'INSERT INTO store (id , store_name,store_location) VALUES (?,?,?)'
   cursor.execute(insert_dummy_store , Store1)
   cursor.execute(insert_dummy_store , Store2)

   connection.commit()

   connection.close()


def all_store():
    query = 'select * from store'
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    row = cursor.execute(query)
    for r in row:
        print(r)

    connection.close()

def all_user():
    query = 'select * from user'
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    row = cursor.execute(query)
    for r in row:
        print(r)

    connection.close()


def process_dummy_operation():
    create_table()

    insert_user()
    #insert_store()

    #all_store()
    #all_user()

