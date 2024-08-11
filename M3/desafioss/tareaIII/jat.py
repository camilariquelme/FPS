def mostrar_menu():
    print("\n--- Menú de Pizza JAT ---")
    print("1. Personalizar Pizza")
    print("2. Ver Ingredientes")
    print("3. Confirmar Pedido")
    print("4. Salir")

def seleccionar_masa():
    masas = ["Tradicional", "Delgada", "Bordes de Queso"]
    print("\nSeleccione el tipo de masa:")
    for i, masa in enumerate(masas, 1):
        print(f"{i}. {masa}")
    opcion = int(input("Opción: "))
    return masas[opcion - 1]

def seleccionar_salsa():
    salsas = ["Tomate", "Alfredo", "Barbecue", "Pesto"]
    print("\nSeleccione el tipo de salsa:")
    for i, salsa in enumerate(salsas, 1):
        print(f"{i}. {salsa}")
    opcion = int(input("Opción: "))
    return salsas[opcion - 1]

def modificar_ingredientes(ingredientes_actuales):
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
    tiempo_base = 20
    tiempo_total = tiempo_base + (len(ingredientes) * 2)
    return tiempo_total

def mostrar_ingredientes(ingredientes):
    if ingredientes:
        print("Ingredientes actuales:", ", ".join(ingredientes))
    else:
        print("No se han seleccionado ingredientes aún.")

def confirmar_pedido(ingredientes, masa, salsa):
    tiempo = calcular_tiempo_preparacion(ingredientes)
    print(f"\nTu pizza con masa {masa} y salsa {salsa} estará lista en {tiempo} minutos.")
    print(f"Ingredientes: {', '.join(ingredientes)}")
    print("¡Gracias por tu pedido!")

def main():
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
