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
        print(f'База данных {name_db} создана')
    except Error as e:
        print(e)

def show_db():
    try:
        with connect(
                host="localhost",
                user='login',
                password='zuFyETV0',
        ) as connection:
            show_db_query = "SHOW DATABASES"
            with connection.cursor() as cursor:
                cursor.execute(show_db_query)
                for db in cursor:
                    print(db)
    except Error as e:
        print(e)

def connect_db(name_db):
    try:
        with connect(
                host="localhost",
                user='login',
                password='zuFyETV0',
                database=name_db,
        ) as connection:
            return connection
    except Error as e:
        print(e)

def send_request(request, name_db, make_print=False): # Используем для создания таблиц в базе данных
    try:
        with connect(
                host="localhost",
                user='login',
                password='zuFyETV0',
                database=name_db,
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(request)
                if make_print:
                    result = cursor.fetchall()
                    for row in result:
                        print(row)
                else:
                    connection.commit()
    except Error as e:
        print(e)


create_movies_table_query = """
CREATE TABLE movies(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    release_year YEAR(4),
    genre VARCHAR(100),
    collection_in_mil INT
)
"""
create_reviewers_table_query = """
CREATE TABLE reviewers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100)
)
"""
create_ratings_table_query = """
CREATE TABLE ratings (
    movie_id INT,
    reviewer_id INT,
    rating DECIMAL(2,1),
    FOREIGN KEY(movie_id) REFERENCES movies(id),
    FOREIGN KEY(reviewer_id) REFERENCES reviewers(id),
    PRIMARY KEY(movie_id, reviewer_id)
)
"""

alter_table_query = """
ALTER TABLE movies
MODIFY COLUMN collection_in_mil DECIMAL(4,1)
"""

# send_request(create_movies_table_query, 'online_movie_rating')
# send_request(create_reviewers_table_query, 'online_movie_rating')
# send_request(create_ratings_table_query, 'online_movie_rating')

# send_request("DESCRIBE movies", 'online_movie_rating', True)

# send_request(alter_table_query, 'online_movie_rating') # Внесли изменения. collection_in_mil INT -> DECIMAL(4,1)
# send_request("DESCRIBE movies", 'online_movie_rating', True)

