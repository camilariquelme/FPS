def mostrar_menu():
    """
    Muestra el menú principal de opciones para el usuario.
    
    Opciones:
    1. Personalizar Pizza
    2. Ver Ingredientes
    3. Confirmar Pedido
    4. Salir
    """
    print("\n--- Menú de Pizza JAT ---")
    print("1. Personalizar Pizza")
    print("2. Ver Ingredientes")
    print("3. Confirmar Pedido")
    print("4. Salir")

def seleccionar_masa():
    """
    Permite al usuario seleccionar el tipo de masa para la pizza.
    
    Retorna:
        str: El tipo de masa seleccionado por el usuario.
    """
    masas = ["Tradicional", "Delgada", "Bordes de Queso"]
    print("\nSeleccione el tipo de masa:")
    for i, masa in enumerate(masas, 1):
        print(f"{i}. {masa}")
    opcion = int(input("Opción: "))
    return masas[opcion - 1]

def seleccionar_salsa():
    """
    Permite al usuario seleccionar el tipo de salsa para la pizza.
    
    Retorna:
        str: El tipo de salsa seleccionado por el usuario.
    """
    salsas = ["Tomate", "Alfredo", "Barbecue", "Pesto"]
    print("\nSeleccione el tipo de salsa:")
    for i, salsa in enumerate(salsas, 1):
        print(f"{i}. {salsa}")
    opcion = int(input("Opción: "))
    return salsas[opcion - 1]

def modificar_ingredientes(ingredientes_actuales):
    """
    Permite al usuario agregar o eliminar ingredientes de la pizza.

    Parámetros:
        ingredientes_actuales (list): Lista de ingredientes actualmente seleccionados.

    Retorna:
        list: Lista actualizada de ingredientes después de la modificación.
    """
    ingredientes = ["Tomate", "Champiñones", "Aceituna", "Cebolla", "Pollo", "Jamón", "Carne", "Tocino", "Queso"]
    while True:
        print("\n--- Modificar Ingredientes ---")
        print("1. Agregar Ingrediente")
        print("2. Eliminar Ingrediente")
        print("3. Volver al Menú Principal")
        opcion = int(input("Opción: "))

        if opcion == 1:
            print("\nSeleccione un ingrediente para agregar:")
            for i, ing in enumerate(ingredientes, 1):
                print(f"{i}. {ing}")
            seleccion = int(input("Opción: "))
            if ingredientes[seleccion - 1] not in ingredientes_actuales:
                ingredientes_actuales.append(ingredientes[seleccion - 1])
                print(f"{ingredientes[seleccion - 1]} agregado.")
            else:
                print(f"{ingredientes[seleccion - 1]} ya está en la pizza.")

        elif opcion == 2:
            if ingredientes_actuales:
                print("\nSeleccione un ingrediente para eliminar:")
                for i, ing in enumerate(ingredientes_actuales, 1):
                    print(f"{i}. {ing}")
                seleccion = int(input("Opción: "))
                eliminado = ingredientes_actuales.pop(seleccion - 1)
                print(f"{eliminado} eliminado de la pizza.")
            else:
                print("No hay ingredientes para eliminar.")

        elif opcion == 3:
            break
        else:
            print("Opción no válida, intente de nuevo.")
    return ingredientes_actuales

def calcular_tiempo_preparacion(ingredientes):
    """
    Calcula el tiempo de preparación de la pizza basado en la cantidad de ingredientes.

    Parámetros:
        ingredientes (list): Lista de ingredientes seleccionados para la pizza.

    Retorna:
        int: Tiempo total de preparación en minutos.
    """
    tiempo_base = 20
    tiempo_total = tiempo_base + (len(ingredientes) * 2)
    return tiempo_total

def mostrar_ingredientes(ingredientes):
    """
    Muestra los ingredientes actuales seleccionados para la pizza.

    Parámetros:
        ingredientes (list): Lista de ingredientes seleccionados.
    """
    if ingredientes:
        print("Ingredientes actuales:", ", ".join(ingredientes))
    else:
        print("No se han seleccionado ingredientes aún.")

def confirmar_pedido(ingredientes, masa, salsa):
    """
    Confirma el pedido de la pizza, mostrando el tiempo de preparación y los ingredientes seleccionados.

    Parámetros:
        ingredientes (list): Lista de ingredientes seleccionados.
        masa (str): Tipo de masa seleccionada.
        salsa (str): Tipo de salsa seleccionada.
    """
    tiempo = calcular_tiempo_preparacion(ingredientes)
    print(f"\nTu pizza con masa {masa} y salsa {salsa} estará lista en {tiempo} minutos.")
    print(f"Ingredientes: {', '.join(ingredientes)}")
    print("¡Gracias por tu pedido!")

def main():
    """
    Función principal que ejecuta el flujo del programa Pizza JAT.
    Permite al usuario personalizar su pizza, ver ingredientes, y confirmar el pedido.
    """
    ingredientes_actuales = []
    masa = seleccionar_masa()
    salsa = seleccionar_salsa()

    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            ingredientes_actuales = modificar_ingredientes(ingredientes_actuales)
        elif opcion == 2:
            mostrar_ingredientes(ingredientes_actuales)
        elif opcion == 3:
            confirmar_pedido(ingredientes_actuales, masa, salsa)
            break
        elif opcion == 4:
            print("Gracias por usar Pizza JAT. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
