import sqlite3


def create_db():
    with open('Script_students_sqlite.sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect('Script_students_sqlite.db') as con:
        cur = con.cursor()
        cur.executescript(sql)


if __name__ == "__main__":
    create_db()
