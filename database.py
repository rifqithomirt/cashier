from datetime import datetime
import sqlite3
conn = sqlite3.connect('flowmeter.db')
jenis= "minyak"
posisi= "outlet"

def createTable( ):
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS flowmeter ( jenis text, posisi text, nilai double, produk text, jam datetime, status text)")
    conn.commit()

def insertValue( jenis, posisi, nilai, produk ):
    c = conn.cursor()
    c.execute("INSERT INTO flowmeter ( jenis, posisi, nilai, produk, jam ) VALUES(?,?,?,?,?)", [ jenis, posisi, nilai, produk, datetime.now() ])
    conn.commit()

def deleteAll( ):
    c = conn.cursor()
    c.execute("DELETE FROM flowmeter WHERE 1")
    conn.commit()

def selectAll( )
    c = conn.cursor()
    for row in c.execute('SELECT * FROM flowmeter'):
            print(row)
    conn.commit()

selectAll( )