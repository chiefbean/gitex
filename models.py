import sqlite3 as sql

def getRepo(name):
    con = sql.connect("data.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from repo where name=?", (name,))
    r = cur.fetchone()

    cur = con.cursor()
    cur.execute("select * from commit where repoid=?", (r['id'],))
    c = cur.fetchall()

    con.close()

    return r, c