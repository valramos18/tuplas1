def hacer_menu():
    print ("1. Registrar nuevo cliente.")
    print ("2. Eliminar cliente.")
    print ("3. actualizar informacion del cliente.")
    print ("0. Salir del sistema.")
    print ("... Seleccione una opcion ...")
    opcion = int(input())
    return opcion

def registrar_cliente():
    nombre_cliente = input("digite el nombre:")
    apellido_cliente = input("digite el apellido:")
    cedula_cliente = input("digite la cedula:")
    inf_cliente_tupla = (nombre_cliente, apellido_cliente, cedula_cliente)
    return inf_cliente_tupla

def guardar_clientes(inf_cliente_tupla, bd_cliente):
    bd_cliente.append(inf_cliente_tupla)
    print("Cliente guardado con éxito.")
    return bd_cliente

def eliminar_cliente(cedula, bd):
    for cliente in bd:
        if cliente[2] == cedula:
            bd.remove(cliente)
            print("Cliente eliminado con éxito.")
            return
    print("Cliente no encontrado.")

def actualizar_cliente(cedula, bd):
    for i, cliente in enumerate(bd):
        if cliente[2] == cedula:
            print("Ingrese los nuevos datos:")
            cliente_lista = list(cliente)
            cliente_lista[0] = input("Nuevo nombre: ")
            cliente_lista[1] = input("Nuevo apellido: ")
            cliente_lista[2] = input("Nueva cédula: ")
            bd[i] = tuple(cliente_lista)
            print(f"Nuevo registro del cliente: {bd[i]}")
            return
        print("Cliente no encontrado.")

# Código principal

base_de_datos = []
while True:
    opcion = hacer_menu()
    match opcion:
        case 1:
            cliente = registrar_cliente()
            guardar_cliente(cliente, base_de_datos)
        case 2:
            cedula = input("Ingrese la cédula del cliente a eliminar: ")
            eliminar_cliente(cedula, base_de_datos)
        case 3:
            cedula = input("Ingrese la cédula del cliente a actualizar: ")
            actualizar_cliente(cedula, base_de_datos)
        case 0:
            print("Saliendo del sistema...")
            break
        case _:
            print("Opción no válida, intente de nuevo.")
