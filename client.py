import Pyro4

product_service = Pyro4.Proxy("PYRONAME:product.service")
purchase_service = Pyro4.Proxy("PYRONAME:purchase.service")

def client_menu():
    while True:
        print("\n--- Menú Cliente ---")
        print("1. Ver productos")
        print("2. Comprar producto")
        print("3. Ver mis compras")
        print("0. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == "1":
            products = product_service.get_products()
            for product in products:
                print(product)
        
        elif choice == "2":
            product_id = int(input("ID del producto: "))
            quantity = int(input("Cantidad: "))
            user_id = int(input("Su ID de usuario: "))
            product = product_service.get_product(product_id)
            purchase_service.buy_product(user_id, product_id, quantity, product[3])

        elif choice == "3":
            user_id = int(input("Su ID de usuario: "))
            purchases = purchase_service.get_purchases(user_id)
            for purchase in purchases:
                print(purchase)

        elif choice == "0":
            break

if __name__ == "__main__":
    client_menu()
