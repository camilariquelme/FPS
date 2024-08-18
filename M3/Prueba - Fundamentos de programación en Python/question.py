import random
from preguntas import pool_preguntas
from shuffle import shuffle_alt

def choose_q(dificultad):
    preguntas_disponibles = list(pool_preguntas[dificultad].keys())
    if not preguntas_disponibles:
        return None, None
    
    pregunta_elegida = random.choice(preguntas_disponibles)
    enunciado = pool_preguntas[dificultad][pregunta_elegida]['enunciado']
    alternativas = shuffle_alt(pool_preguntas[dificultad][pregunta_elegida])
    
    # Eliminamos esta línea para no borrar la pregunta del pool
    # del pool_preguntas[dificultad][pregunta_elegida]
    
    return enunciado, alternativas

if __name__ == '__main__':
    # Test
    enunciado, alternativas = choose_q('basicas')
    print(f"Enunciado: {enunciado}")
    print(f"Alternativas: {alternativas}")