import sqlite3
from sqlite3 import Error


def __create_connection(db_name: str):
    conn = None
    try:
        # create if not exists and connect
        conn = sqlite3.connect(db_name)
        return conn
    except Error as e:
        print(e)

    return conn


def __create_table(conn, create_table_sql):
    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
        conn.commit()
        cur.close()
        print("Table exists.")
    except Error as e:
        print(e)


def __add_entry(conn, entry):
    try:
        sql = "INSERT INTO recipes(title, recipe, dish) VALUES(?,?,?)"
        cur = conn.cursor()
        cur.execute(sql, entry)
        conn.commit()
        cur.close()
        conn.close()
        print("Data successfully added to cookbook.")
    except Error as e:
        print(e)


def add(title: str, recipe: str, dish: str):
    """
    Add recipe to database
    """
    database = 'cookbook.sqlite3'

    sql_create_table = """ CREATE TABLE IF NOT EXISTS recipes (
                                        id integer PRIMARY KEY,
                                        title text NOT NULL,
                                        recipe text,
                                        dish text
                                    ); """

    conn = __create_connection(database)

    if conn is not None:
        __create_table(conn, sql_create_table)

        entry = (title, recipe, dish)
        __add_entry(conn, entry)
        return True
    else:
        print("Connection error.")
        return False

