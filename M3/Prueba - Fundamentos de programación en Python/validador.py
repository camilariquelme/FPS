def validate(opciones, eleccion):
    while eleccion not in opciones:
        print(f"Opción no válida, ingrese una de las opciones válidas: {opciones}")
        eleccion = input("Ingrese su elección: ")
    return eleccion

if __name__ == '__main__':
    # Test
    opciones = ['1', '2', '3']
    eleccion = input("Ingrese una opción (1, 2 o 3): ")
    resultado = validate(opciones, eleccion)
    print(f"Opción válida seleccionada: {resultado}")