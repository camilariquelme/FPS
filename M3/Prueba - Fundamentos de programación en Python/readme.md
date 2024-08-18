# Trivia Interactiva en Python

Este proyecto es una aplicación de trivia interactiva desarrollada en Python. La aplicación permite a los usuarios jugar una trivia con preguntas de diferentes niveles de dificultad.

## Características

    - Tres niveles de dificultad: Básica, Intermedia y Avanzada.
    - Número configurable de preguntas por nivel.
    - Preguntas y alternativas presentadas en orden aleatorio.
    - Validación de entradas del usuario.
    - Contador de puntaje.

## Estructura del Proyecto

El proyecto está compuesto por los siguientes archivos:

    - `main.py`: Archivo principal que ejecuta la trivia.
    - `validador.py`: Contiene la función para validar entradas del usuario.
    - `level.py`: Determina el nivel de dificultad de cada pregunta.
    - `shuffle.py`: Mezcla las alternativas de las preguntas.
    - `question.py`: Selecciona preguntas aleatorias del pool de preguntas.
    - `print_preguntas.py`: Formatea y muestra las preguntas y alternativas.
    - `verify.py`: Verifica si la respuesta del usuario es correcta.
    - `preguntas.py`: Contiene el pool de preguntas y alternativas.

## Cómo jugar

    1. Ejecute `main.py`.
    2. Elija comenzar el juego o salir.
    3. Seleccione el número de preguntas por nivel (1, 2 o 3).
    4. Responda las preguntas seleccionando la letra correspondiente a la alternativa correcta.
    5. Al final del juego, se mostrará su puntaje total.
    6. Puede elegir jugar de nuevo o salir.

## Requisitos

- Python 3.x

## Instalación

    1. Clone este repositorio o descargue los archivos.
    2. Asegúrese de tener Python 3.x instalado en su sistema.
    3. No se requieren dependencias adicionales.

## Ejecución

Para iniciar la trivia, ejecute el siguiente comando en la terminal:

   python main.py

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abra un issue para discutir cambios mayores antes de realizar un pull request.
