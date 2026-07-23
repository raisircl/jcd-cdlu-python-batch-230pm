import sqlite3

conn=sqlite3.connect('college.db')

cursor=conn.cursor()
print("Database created and opened successfully")

cursor.execute('''CREATE TABLE IF NOT EXISTS tbl_students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    attendance REAL,
    marks REAL,
    result TEXT
)
''')
print("Table created successfully")
conn.close()
