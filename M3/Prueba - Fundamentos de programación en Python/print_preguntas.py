def print_pregunta(enunciado, alternativas):
    print(enunciado)
    print()
    letras = ['A', 'B', 'C', 'D']
    for i, alternativa in enumerate(alternativas):
        print(f"{letras[i]}. {alternativa[0]}")

if __name__ == '__main__':
    # Test
    enunciado = "¿Cuál es la capital de Francia?"
    alternativas = [
        ["Londres", 0],
        ["París", 1],
        ["Roma", 0],
        ["Madrid", 0]
    ]
    print_pregunta(enunciado, alternativas)