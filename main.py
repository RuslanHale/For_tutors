from getpass import getpass
from mysql.connector import connect, Error

def create_db(name_db):
    try:
        with connect(
            host="localhost",
            user='login',
            password='zuFyETV0',
        ) as connection:
            create_db_query = f"CREATE DATABASE {name_db}"
            with connection.cursor() as cursor:
                cursor.execute(create_db_query)
    except Error as e:
        print(e)

def show_db():
    try:
        with connect(
                host="localhost",
                user='root',
                password='zuFyETV0',
        ) as connection:
            show_db_query = "SHOW DATABASES"
            with connection.cursor() as cursor:
                cursor.execute(show_db_query)
                for db in cursor:
                    print(db)
    except Error as e:
        print(e)

create_db('makar')
show_db()