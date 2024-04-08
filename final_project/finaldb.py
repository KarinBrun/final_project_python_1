import sqlite3
from sqlite3 import Error


def create_connection(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None


def create_table(conn, sql_create_table):
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)


def create_tables(database):

    sql_create_character_table = """ CREATE TABLE IF NOT EXISTS character (
                                        id integer PRIMARY KEY,
                                        helm text NOT NULL,
                                        weapon text NOT NULL,
                                        chest text NOT NULL,
                                        gloves text NOT NULL,
                                        boots text NOT NULL,
                                        name text NOT NULL,
                                        race text NOT NULL,
                                        char_class text NOT NULL,
                                        background text NOT NULL
                                    ); """
    print("Creating the connection")
    conn = create_connection(database)
    if conn is not None:
        print("Creating tables")
        create_table(conn, sql_create_character_table)
    else:
        print("Unable to connect to " + str(database))
    conn.commit()


def select_all_characters(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM character")
    rows = cur.fetchall()
    return rows


def select_character_by_id(conn, character_id):
    cur = conn.cursor()
    sql = '''SELECT * FROM character WHERE id = ?'''
    cur.execute(sql, (character_id,))
    print("Getting character")
    rows = cur.fetchall()
    print(rows)
    return rows[0]


def create_character(conn, character):
    sql = ''' INSERT INTO character(helm,weapon,chest,gloves,boots,name,race,char_class,background)
              VALUES(?,?,?,?,?,?,?,?,?) '''
    print("Connecting to database")
    cur = conn.cursor()
    print("Creating character")
    cur.execute(sql, character)
    conn.commit()
    print(cur.lastrowid)
    return cur.lastrowid


def update_character(conn, character):
    sql = ''' UPDATE character
              SET helm = ?,
                  weapon = ?,
                  chest = ?,
                  gloves = ?,
                  boots = ?,
                  name = ?,
                  race = ?,
                  char_class = ?,
                  background = ?
              WHERE id = ?'''
    print("Connecting to database")
    cur = conn.cursor()
    print("Updating character")
    cur.execute(sql, character)
    conn.commit()


def delete_character(conn, character_id):
    sql = '''DELETE FROM character WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, (character_id,))
    conn.commit()


if __name__ == '__main__':
    create_tables("finalProject.db")
