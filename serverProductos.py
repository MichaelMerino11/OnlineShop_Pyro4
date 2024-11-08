'''
Francisco López
Micahel Merino
Alexandro Mendoza
Brayan Barrero
'''
import sqlite3
import Pyro4

def init_db():
    conn = sqlite3.connect("productos.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            unidades INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@Pyro4.expose
class ProductServer:
    def __init__(self):
        init_db()

    def agregar_producto(self, nombre, precio, unidades):
        conn = sqlite3.connect("productos.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos (nombre, precio, unidades) VALUES (?, ?, ?)", (nombre, precio, unidades))
        conn.commit()
        conn.close()
        return "Producto agregado correctamente."

    def listar_productos(self):
        conn = sqlite3.connect("productos.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        conn.close()
        return productos

    def actualizar_producto(self, id_producto, nombre=None, precio=None, unidades=None):
        conn = sqlite3.connect("productos.db")
        cursor = conn.cursor()
        if nombre:
            cursor.execute("UPDATE productos SET nombre = ? WHERE id = ?", (nombre, id_producto))
        if precio:
            cursor.execute("UPDATE productos SET precio = ? WHERE id = ?", (precio, id_producto))
        if unidades:
            cursor.execute("UPDATE productos SET unidades = ? WHERE id = ?", (unidades, id_producto))
        conn.commit()
        conn.close()
        return "Producto actualizado correctamente."

    def eliminar_producto(self, id_producto):
        conn = sqlite3.connect("productos.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conn.commit()
        conn.close()
        return "Producto eliminado correctamente."


def start_server():
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(ProductServer)
    ns.register("product.server", uri)
    print("Servidor de productos iniciado.")
    daemon.requestLoop()

if __name__ == "__main__":
    start_server()
