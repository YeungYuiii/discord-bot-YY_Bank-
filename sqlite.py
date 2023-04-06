import sqlite3 as sl

#conn = sl.connect(':memory:')
conn = sl.connect('cy_bank.db')
print("database accessed successfully")

c = conn.cursor()

c.execute("""
    CREATE TABLE USER (
        id TEXT NOT NULL PRIMARY KEY,
        name TEXT,
        balance REAL
    );
    """)

c.execute("""
    CREATE TABLE TRAN (
        transaction_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        id TEXT NOT NULL,
        date TEXT,
        type BOOELAN,
        amount REAL,
        message TEXT
    );
    """)

c.execute("INSERT INTO USER (id,name,balance) VALUES ('471515187674087434', 'YCY', 0)")

conn.commit()
conn.close()