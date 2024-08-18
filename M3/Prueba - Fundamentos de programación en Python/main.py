
import preguntas as p
from question import choose_q
from print_preguntas import print_pregunta
from level import choose_level
from validador import validate
from level import choose_level
from verify import verificar
import time
import os
import sys

def main():
    print("¡Bienvenido a la Trivia!")
    
    while True:
        opcion = validate(['0', '1'], input("Ingrese 1 para comenzar o 0 para salir: "))
        if opcion == '0':
            print("Nos vemos pronto!")
            break
        
        n_preguntas_por_nivel = int(validate(['1', '2', '3'], input("Ingrese el número de preguntas por nivel (1, 2 o 3): ")))
        total_preguntas = n_preguntas_por_nivel * 3
        
        n_pregunta = 1
        puntaje = 0
        
        while n_pregunta <= total_preguntas:
            nivel = choose_level(n_pregunta, n_preguntas_por_nivel)
            enunciado, alternativas = choose_q(nivel)
            
            if enunciado is None:
                print(f"No hay más preguntas disponibles en el nivel {nivel}.")
                break
            
            print(f"\nPregunta {n_pregunta}:")
            print_pregunta(enunciado, alternativas)
            
            respuesta = validate(['A', 'B', 'C', 'D'], input("Ingrese su respuesta (A, B, C o D): "))
            
            if verificar(alternativas, respuesta):
                puntaje += 1
            
            n_pregunta += 1
        
        print(f"\n¡Juego terminado! Tu puntaje final es: {puntaje}/{total_preguntas}")
        
        continuar = validate(['0', '1'], input("¿Desea jugar de nuevo? (1: Sí, 0: No): "))
        if continuar == '0':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

if __name__ == "__main__":
    main()