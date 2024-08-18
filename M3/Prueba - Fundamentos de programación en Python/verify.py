def verificar(alternativas, eleccion):
    letra_a_indice = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
    indice_elegido = letra_a_indice[eleccion.upper()]
    
    if alternativas[indice_elegido][1] == 1:
        print("Respuesta Correcta")
        return True
    else:
        print("Respuesta Incorrecta")
        return False

if __name__ == '__main__':
    # Test
    alternativas = [
        ["Londres", 0],
        ["París", 1],
        ["Roma", 0],
        ["Madrid", 0]
    ]
    eleccion = input("Ingrese su respuesta (A, B, C o D): ")
    verificar(alternativas, eleccion)