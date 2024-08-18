# preguntas.py

preguntas_basicas = {
    'pregunta_1': {
        'enunciado': '¿Cuál es la capital de Francia?',
        'alternativas': [
            ['Londres', 0],
            ['París', 1],
            ['Roma', 0],
            ['Madrid', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': '¿Cuál es el planeta más grande del sistema solar?',
        'alternativas': [
            ['Marte', 0],
            ['Júpiter', 1],
            ['Saturno', 0],
            ['Neptuno', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': '¿Cuál es el océano más grande?',
        'alternativas': [
            ['Atlántico', 0],
            ['Pacífico', 1],
            ['Índico', 0],
            ['Ártico', 0]
        ]
    }
}

preguntas_intermedias = {
    'pregunta_1': {
        'enunciado': '¿En qué año comenzó la Primera Guerra Mundial?',
        'alternativas': [
            ['1905', 0],
            ['1914', 1],
            ['1918', 0],
            ['1939', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': '¿Cuál es el elemento químico más abundante en el universo?',
        'alternativas': [
            ['Oxígeno', 0],
            ['Hidrógeno', 1],
            ['Carbono', 0],
            ['Helio', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': '¿Quién pintó "La noche estrellada"?',
        'alternativas': [
            ['Pablo Picasso', 0],
            ['Vincent van Gogh', 1],
            ['Claude Monet', 0],
            ['Salvador Dalí', 0]
        ]
    }
}

preguntas_avanzadas = {
    'pregunta_1': {
        'enunciado': '¿Cuál es la partícula subatómica más pesada?',
        'alternativas': [
            ['Electrón', 0],
            ['Quark top', 1],
            ['Protón', 0],
            ['Neutrón', 0]
        ]
    },
    'pregunta_2': {
        'enunciado': '¿Qué científico propuso la teoría de la relatividad general?',
        'alternativas': [
            ['Isaac Newton', 0],
            ['Albert Einstein', 1],
            ['Stephen Hawking', 0],
            ['Niels Bohr', 0]
        ]
    },
    'pregunta_3': {
        'enunciado': '¿En qué año se descubrió la estructura del ADN?',
        'alternativas': [
            ['1943', 0],
            ['1953', 1],
            ['1963', 0],
            ['1973', 0]
        ]
    }
}

pool_preguntas = {
    'basicas': preguntas_basicas,
    'intermedias': preguntas_intermedias,
    'avanzadas': preguntas_avanzadas
}