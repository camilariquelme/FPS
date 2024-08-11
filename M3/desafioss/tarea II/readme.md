# Desafío Evaluado - Estructuras de Datos y Funciones (II)

Este proyecto contiene la solución a tres desafíos relacionados con estructuras de datos y funciones en Python. Cada desafío está implementado en un archivo separado y se puede ejecutar desde la línea de comandos.

## Contenido

1. **Filtrado Relevante (`filtro.py`)**
   - **Descripción:** Este script filtra productos de una tienda según un umbral de precio. Puedes filtrar los productos que tienen un precio mayor o menor que el umbral especificado.
   - **Funcionamiento:**
     - El programa solicita una lista de productos con sus precios.
     - Filtra los productos que tienen un precio mayor o menor que un umbral especificado.
     - Muestra los productos filtrados con sus respectivos precios.
   - **Ejecución:**
     ```bash
     python filtro.py <umbral> [condicion]
     ```
     - `umbral`: Valor de precio para filtrar.
     - `condicion` (opcional): Puede ser "mayor" o "menor". Por defecto es "mayor".
   - **Ejemplo:**
     ```bash
     python filtro.py 30000
     ```
     Resultará en los productos con precio mayor a 30,000.

2. **Alertas Telemáticas (`velocidad.py`)**
   - **Descripción:** Este script calcula las posiciones de las correas transportadoras cuya velocidad supera el promedio de la lista dada.
   - **Funcionamiento:**
     - El programa recibe una lista de velocidades de correas transportadoras.
     - Calcula el promedio de las velocidades.
     - Identifica y muestra las posiciones de las velocidades que están por encima del promedio.
   - **Ejecución:**
     ```bash
     python velocidad.py
     ```
     El script imprimirá una lista con las posiciones que están por encima del promedio.

3. **Apoyo Matemático (`ong.py`)**
   - **Descripción:** Este script incluye funciones para calcular el factorial y la productoria de números. Se puede invocar una función que calcule múltiples operaciones a la vez.
   - **Funcionamiento:**
     - El programa incluye dos funciones principales: una para calcular el factorial de un número y otra para calcular la productoria de una lista de números.
     - Se puede llamar una función controladora que ejecuta ambas operaciones según las necesidades del usuario.
   - **Ejecución:**
     ```bash
     python ong.py
     ```
     - Puedes modificar el código para invocar la función `calcular()` con diferentes valores.
   - **Ejemplo:**
     ```python
     calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)
     ```
     Resultará en la impresión del factorial de 5, la productoria de la lista `[3, 6, 4, 2, 8]`, y el factorial de 6.

## Requisitos

- **Python 3.x**: Asegúrate de tener instalada una versión compatible de Python.

## Instalación del Proyecto

1. Clonar el repositorio:
    ```bash
    git clone <URL_del_repositorio>
    ```

2. Ingresar a la carpeta del proyecto:
    ```bash
    cd nombre-del-proyecto
    ```

3. Ejecutar el script deseado:
    ```bash
    python <nombre_del_script.py>
    ```

## Autor

- [Camila Riquelme](https://github.com/camilariquelme)
