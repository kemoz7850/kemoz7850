import sqlite3
conn = sqlite3.connect('accounts.db')
width = '15'
height = '10'
lenbutton = '500'
ggg = [('15','62',),('6','10',),]
lst = [width,height,lenbutton]
cun = conn.cursor()
cun.execute('''CREATE TABLE IF NOT EXISTS database (
    cata     TEXT,
    ID       TEXT,
    [order]  TEXT,
    suborder TEXT,
    name     TEXT,
    email    TEXT,
    password TEXT,
    color    TEXT DEFAULT ('6e40c0') 
);''')
sql = ''' INSERT INTO database(cata,ID)
              VALUES(?,?) '''
cun.execute(sql, ID)
conn.commit()
data = cun.execute('''SELECT cata FROM database''')
for i in data:
    print(i)

conn.close()