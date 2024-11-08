import Pyro4
import sqlite3

@Pyro4.expose
class ProductService:
    def __init__(self):
        self.conn = sqlite3.connect('database/products.db')
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    quantity INTEGER,
                    description TEXT,
                    price REAL
                )
            ''')

    def add_product(self, name, quantity, description, price):
        with self.conn:
            self.conn.execute("INSERT INTO products (name, quantity, description, price) VALUES (?, ?, ?, ?)", 
                              (name, quantity, description, price))
            print(f"Producto {name} agregado con éxito")

    def get_products(self):
        cursor = self.conn.execute("SELECT * FROM products")
        return cursor.fetchall()

    def edit_product(self, product_id, name, quantity, description, price):
        with self.conn:
            self.conn.execute("UPDATE products SET name=?, quantity=?, description=?, price=? WHERE id=?", 
                              (name, quantity, description, price, product_id))

    def delete_product(self, product_id):
        with self.conn:
            self.conn.execute("DELETE FROM products WHERE id=?", (product_id,))

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(ProductService)
ns.register("product.service", uri)  # Registro en el Name Server con nombre "product.service"
print("ProductService running. URI:", uri)
daemon.requestLoop()