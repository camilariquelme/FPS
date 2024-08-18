import random

def shuffle_alt(pregunta):
    alternativas = pregunta['alternativas']
    random.shuffle(alternativas)
    return alternativas

if __name__ == '__main__':
    # Test
    from preguntas import pool_preguntas
    pregunta = pool_preguntas['basicas']['pregunta_1']
    print(shuffle_alt(pregunta))