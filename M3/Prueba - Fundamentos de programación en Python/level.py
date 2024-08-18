def choose_level(n_pregunta, n_preguntas_por_nivel):
    if n_preguntas_por_nivel == 1:
        if n_pregunta <= 1:
            return 'basicas'
        elif n_pregunta <= 2:
            return 'intermedias'
        else:
            return 'avanzadas'
    elif n_preguntas_por_nivel == 2:
        if n_pregunta <= 2:
            return 'basicas'
        elif n_pregunta <= 4:
            return 'intermedias'
        else:
            return 'avanzadas'
    else:  # n_preguntas_por_nivel == 3
        if n_pregunta <= 3:
            return 'basicas'
        elif n_pregunta <= 6:
            return 'intermedias'
        else:
            return 'avanzadas'

if __name__ == '__main__':
    # Test
    print(choose_level(2, 2))  # Debe imprimir 'basicas'
    print(choose_level(4, 2))  # Debe imprimir 'intermedias'
    print(choose_level(6, 2))  # Debe imprimir 'avanzadas'