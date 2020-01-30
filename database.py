import sqlite3
DB_NAME = 'cheap_OLX.db'

conn = sqlite3.connect(DB_NAME)

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS users
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT ,
        email TEXT UNIQUE,
        password TEXT,
        phone_number INTEGER,
        address TEXT
    )'''
    )

conn.cursor().execute(
    '''
    CREATE TABLE IF NOT EXISTS ads
    (
        id_ad INTEGER PRIMARY KEY AUTOINCREMENT,
        name_ad TEXT,
        info_ad TEXT,
        price INTEGER, 
        date TEXT,
        is_active INTEGER,
        buyer INTEGER
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
  
    )
    '''


)

class DB:
    def __enter__(self):
        self.conn = sqlite3.connect(DB_NAME)
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()