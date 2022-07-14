import sqlite3

def create(dbname ):
    con = sqlite3.connect(dbname)
    con.execute("CREATE TABLE IF NOT EXIST BOOKS(NAME TEXT,PRICE INT,AVAIL TEXT)")
    con.close()

def insert_datato_db(dbname ,values):
    con = sqlite3.connect(dbname)
    con.execute("INSERT  BOOKS(NAME,PRICE,AVAIL) VALUES(?,?,?)",values)
    con.commit()
    con.close()

def get_datafrom_db(dbname ):
    con = sqlite3.connect(dbname)
    cu = con.cursor()
    cu.execute("SELECT * FROM BOOKS")
    data = cu.fetchall()
    for k in data :
        print(k)
        con.close()