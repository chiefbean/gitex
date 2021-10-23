import sqlite3 as sql

def getRepo(id):
    con = sql.connect("data.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from repo where id=?", (id,))
    r = cur.fetchone()
    con.close()

    return r