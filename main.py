from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user='login',
        password='zuFyETV0',
    ) as connection:
        print(connection)
except Error as e:
    print(e)