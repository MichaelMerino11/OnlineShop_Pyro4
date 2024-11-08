'''
Francisco López
Micahel Merino
Alexandro Mendoza
Brayan Barrero
'''
import Pyro4

product_server = Pyro4.Proxy("PYRONAME:product.server")
admin_server = Pyro4.Proxy("PYRONAME:admin.server")

def menu_administrador():
    while True:
        print("\n--- Menú Administrador ---")
        print("1. Agregar Cliente")
        print("2. Listar Clientes")
        print("3. Actualizar Cliente")
        print("4. Eliminar Cliente")
        print("5. Agregar Producto")
        print("6. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            correo = input("Ingrese el correo del cliente: ")
            print(admin_server.agregar_cliente(nombre, correo))
        elif opcion == "2":
            clientes = admin_server.listar_clientes()
            print("\n--- Lista de Clientes ---")
            for cliente in clientes:
                print(f"ID: {cliente[0]}, Nombre: {cliente[1]}, Correo: {cliente[2]}")
        elif opcion == "3":
            id_cliente = int(input("Ingrese el ID del cliente a actualizar: "))
            nombre = input("Nuevo nombre (deje en blanco para no cambiar): ")
            correo = input("Nuevo correo (deje en blanco para no cambiar): ")
            print(admin_server.actualizar_cliente(id_cliente, nombre or None, correo or None))
        elif opcion == "4":
            id_cliente = int(input("Ingrese el ID del cliente a eliminar: "))
            print(admin_server.eliminar_cliente(id_cliente))
        elif opcion == "5":
            nombre_producto = input("Ingrese el nombre del producto: ")
            precio_producto = float(input("Ingrese el precio del producto: "))
            unidades_producto = int(input("Ingrese la cantidad de unidades: "))
            print(product_server.agregar_producto(nombre_producto, precio_producto, unidades_producto))
        elif opcion == "6":
            break
        else:
            print("Opción inválida, intente de nuevo.")

def menu_usuario():
    carrito = []
    total = 0

    while True:
        print("\n--- Menú Usuario ---")
        print("1. Listar Productos")
        print("2. Agregar Producto al Carrito")
        print("3. Finalizar Compra")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            productos = product_server.listar_productos()
            print("\n--- Lista de Productos ---")
            for producto in productos:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}, Unidades disponibles: {producto[3]}")
        elif opcion == "2":
            id_producto = int(input("Ingrese el ID del producto a agregar: "))
            cantidad = int(input("Ingrese la cantidad: "))
            producto = next((p for p in product_server.listar_productos() if p[0] == id_producto), None)
            
            if producto and cantidad <= producto[3]:
                total += producto[2] * cantidad
                carrito.append((producto[1], producto[2], cantidad, producto[2] * cantidad))
                product_server.actualizar_producto(id_producto, unidades=producto[3] - cantidad)
                print(f"{cantidad} unidad(es) de '{producto[1]}' agregado(s) al carrito.")
            else:
                print("Producto no encontrado o cantidad excede el stock disponible.")
        elif opcion == "3":
            if carrito:
                print("\n--- Factura ---")
                for item in carrito:
                    print(f"Producto: {item[0]}, Precio Unitario: {item[1]}, Cantidad: {item[2]}, Subtotal: {item[3]}")
                print(f"Total a pagar: ${total:.2f}")
                carrito.clear()
                total = 0
            else:
                print("El carrito está vacío.")
            break
        elif opcion == "4":
            break
        else:
            print("Opción inválida, intente de nuevo.")

def main_menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Administrador")
        print("2. Usuario")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_administrador()
        elif opcion == "2":
            menu_usuario()
        elif opcion == "3":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main_menu()
