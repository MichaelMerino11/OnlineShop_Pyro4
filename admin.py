import Pyro4

user_service = Pyro4.Proxy("PYRONAME:user.service")
product_service = Pyro4.Proxy("PYRONAME:product.service")

def admin_menu():
    while True:
        print("\n--- Menú Administrador ---")
        print("1. Agregar usuario")
        print("2. Ver usuarios")
        print("3. Agregar producto")
        print("4. Ver productos")
        print("5. Editar producto")
        print("6. Eliminar producto")
        print("0. Salir")

        choice = input("Seleccione una opción: ")
        
        if choice == "1":
            username = input("Nombre de usuario: ")
            id_number = input("Cédula: ")
            email = input("Correo: ")
            user_service.add_user(username, id_number, email)
        
        elif choice == "2":
            users = user_service.get_users()
            for user in users:
                print(user)
        
        elif choice == "3":
            name = input("Nombre del producto: ")
            quantity = int(input("Cantidad: "))
            description = input("Descripción: ")
            price = float(input("Precio: "))
            product_service.add_product(name, quantity, description, price)
        
        elif choice == "4":
            products = product_service.get_products()
            for product in products:
                print(product)
        
        elif choice == "5":
            product_id = int(input("ID del producto: "))
            name = input("Nuevo nombre: ")
            quantity = int(input("Nueva cantidad: "))
            description = input("Nueva descripción: ")
            price = float(input("Nuevo precio: "))
            product_service.edit_product(product_id, name, quantity, description, price)
        
        elif choice == "6":
            product_id = int(input("ID del producto a eliminar: "))
            product_service.delete_product(product_id)
        
        elif choice == "0":
            break

if __name__ == "__main__":
    admin_menu()
