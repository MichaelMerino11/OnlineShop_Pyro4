import Pyro4
import sqlite3

@Pyro4.expose
class UserService:
    def __init__(self):
        self.conn = sqlite3.connect('database/users.db')
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    id_number TEXT,
                    email TEXT
                )
            ''')

    def add_user(self, username, id_number, email):
        with self.conn:
            self.conn.execute("INSERT INTO users (username, id_number, email) VALUES (?, ?, ?)", 
                              (username, id_number, email))

    def get_users(self):
        cursor = self.conn.execute("SELECT * FROM users")
        return cursor.fetchall()

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(UserService)
ns.register("user.service", uri)  # Registro en el Name Server con nombre "user.service"
print("UserService running. URI:", uri)
daemon.requestLoop()
