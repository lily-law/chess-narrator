import sqlite3
from sqlite3 import Error

# DB setup as described in https://www.sqlitetutorial.net/sqlite-python/create-tables/

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def SQL(db_file_path):
    database = db_file_path

    sql_create_people_table = """CREATE TABLE IF NOT EXISTS people (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                avatar text,
                                link text,
                                is_user bool
                            );"""

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        person_id integer NOT NULL,
                                        email_hash text NOT NULL,
                                        password_hash text NOT NULL,
                                        username text NOT NULL,
                                        email_confirmed text,
                                        FOREIGN KEY (person_id) REFERENCES people (id)
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create users table
        create_table(conn, sql_create_users_table)

        # create people table
        create_table(conn, sql_create_people_table)

        return conn
    else:
        print("Error! cannot create the database connection.")


