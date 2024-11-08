'''
Francisco López
Micahel Merino
Alexandro Mendoza
Brayan Barrero
'''
import sqlite3
import Pyro4

def init_db():
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

@Pyro4.expose
class AdminServer:
    def __init__(self):
        init_db()

    def agregar_cliente(self, nombre, correo):
        conn = sqlite3.connect("clientes.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nombre, correo) VALUES (?, ?)", (nombre, correo))
        conn.commit()
        conn.close()
        return "Cliente agregado correctamente."

    def listar_clientes(self):
        conn = sqlite3.connect("clientes.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        conn.close()
        return clientes

    def actualizar_cliente(self, id_cliente, nombre=None, correo=None):
        conn = sqlite3.connect("clientes.db")
        cursor = conn.cursor()
        if nombre:
            cursor.execute("UPDATE clientes SET nombre = ? WHERE id = ?", (nombre, id_cliente))
        if correo:
            cursor.execute("UPDATE clientes SET correo = ? WHERE id = ?", (correo, id_cliente))
        conn.commit()
        conn.close()
        return "Cliente actualizado correctamente."

    def eliminar_cliente(self, id_cliente):
        conn = sqlite3.connect("clientes.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
        conn.commit()
        conn.close()
        return "Cliente eliminado correctamente."


def start_admin_server():
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(AdminServer)
    ns.register("admin.server", uri)
    print("Servidor de administración de clientes iniciado.")
    daemon.requestLoop()

if __name__ == "__main__":
    start_admin_server()
