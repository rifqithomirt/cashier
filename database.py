from datetime import datetime
import sqlite3
conn = sqlite3.connect('flowmeter.db')
jenis= "minyak"
posisi= "outlet"

def createTable( ):
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS flowmeter ( jenis text, posisi text, nilai double, produk text, jam datetime, status text)")
    conn.commit()

def insertValue( jenis, posisi, nilai, produk , jam):
    c = conn.cursor()
    c.execute("INSERT INTO flowmeter ( jenis, posisi, nilai, produk, jam ) VALUES(?,?,?,?,?)", [ jenis, posisi, nilai, produk, jam ])
    conn.commit()

def updateValue( nilai, jam ):
    c = conn.cursor()
    c.execute("UPDATE flowmeter SET nilai='"+ str(nilai) +"' WHERE jam='" + jam + "'")
    conn.commit()

def deleteAll( ):
    c = conn.cursor()
    c.execute("DELETE FROM flowmeter WHERE 1")
    conn.commit()

def selectAll( ):
    c = conn.cursor()
    for row in c.execute('SELECT * FROM flowmeter'):
            print(row)
    conn.commit()

def getTodayTotalizer():
    now = datetime.now();
    dateOnly = now.strftime("%Y-%m-%d")
    c = conn.cursor()
    arrayResult = c.execute('SELECT * FROM flowmeter WHERE jam = "' + dateOnly + '"')
    conn.commit()
    old_nilai = 0
    for row in arrayResult:
        old_nilai = row[2]
    return old_nilai
        
def setByDay( nilai ):
    now = datetime.now();
    dateOnly = now.strftime("%Y-%m-%d")
    c = conn.cursor()
    arrayResult = c.execute('SELECT * FROM flowmeter WHERE jam = "' + dateOnly + '"')
    old_nilai = 0
    count = 0
    for row in arrayResult:
        old_nilai = row[2]
        count = count + 1
    if( old_nilai != nilai ):
        print('tidaksama')
        if( count == 1 ):
            updateValue( nilai, dateOnly )
            conn.commit()
        elif( count == 0 ): 
            insertValue(jenis, posisi, nilai, jenis, dateOnly)
            conn.commit()
    else: 
        print('sama')
    
selectAll()
