import Pyro4
import sqlite3

@Pyro4.expose
class PurchaseService:
    def __init__(self):
        self.conn = sqlite3.connect('database/purchases.db')
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS purchases (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    product_id INTEGER,
                    quantity INTEGER,
                    total_price REAL
                )
            ''')

    def buy_product(self, user_id, product_id, quantity, price):
        total_price = quantity * price
        with self.conn:
            self.conn.execute("INSERT INTO purchases (user_id, product_id, quantity, total_price) VALUES (?, ?, ?, ?)", 
                              (user_id, product_id, quantity, total_price))

    def get_purchases(self, user_id=None):
        query = "SELECT * FROM purchases"
        if user_id:
            query += " WHERE user_id = ?"
            cursor = self.conn.execute(query, (user_id,))
        else:
            cursor = self.conn.execute(query)
        return cursor.fetchall()

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(PurchaseService)
ns.register("product.service", uri)
print("PurchaseService running. URI:", uri)
daemon.requestLoop()