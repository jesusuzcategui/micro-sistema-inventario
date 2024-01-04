import sqlite3
import uuid

class Db:
    def __init__(self):
        self.localDb = sqlite3.connect('basededatos.db')
        self.cursor = self.localDb.cursor()
    
    def inizialite(self):
        try:
            self.cursor.execute('''
                                CREATE TABLE products(
                                    title TEXT NOT NULL,
                                    stock INTEGER NOT NULL DEFAULT 0, 
                                    price INTEGER NOT NULL, 
                                    price_sale INTEGER NOT NULL,
                                    owner_id INTEGER NOT NULL DEFAULT 0,
                                    status INTEGER NOT NULL DEFAULT 1)
                                ''')
            return True
        except Exception as e:
            return False
    
    def create(self, name, stock, price, price_sale, owner):
        try:
            
            self.cursor.execute('''
                                INSERT INTO products(title, stock, price, price_sale, status, owner_id)
                                VALUES (?, ?, ?, ?, ?, ?)
                                ''', (name, stock, price, price_sale, 1, owner))

            self.localDb.commit()
            return True
        except Exception as e:
            print(e)
            return False
    
    def update(self, name, path, id):
        try:
            self.cursor.execute('''
                UPDATE shops SET nameshop = ?, path = ?
                WHERE rowid = ?
            ''', (name, path, id,))

            self.localDb.commit()
            return True
        except Exception as e:
            return e
    
    def delete(self, id):
        try:
            self.cursor.execute('''
                DELETE FROM shops
                WHERE rowid = ?
            ''', (id,))

            self.localDb.commit()
            return True
        except Exception as e:
            return e
    
    def list(self):
        try:
            self.cursor.execute('''
                    SELECT rowid, title, stock, price, price_sale, IIF(owner_id == 1, 'Tia chavela', 'Mio') owner_name, status FROM products
                ''')
            return self.cursor.fetchall()
        except Exception as e:
            return e