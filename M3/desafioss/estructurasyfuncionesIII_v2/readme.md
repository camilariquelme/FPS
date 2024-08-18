Proyecto Pizza JAT

Este proyecto simula un sistema interactivo de personalización y pedido de pizzas. El programa permite a los usuarios seleccionar la masa y la salsa de su pizza, agregar o eliminar ingredientes, y confirmar su pedido final. El tiempo de preparación de la pizza se calcula en función del número de ingredientes seleccionados.

Funcionalidades Principales

Personalizar Pizza: Los usuarios pueden agregar o eliminar ingredientes de su pizza.
Ver Ingredientes: Los usuarios pueden revisar los ingredientes seleccionados hasta el momento.
Confirmar Pedido: El sistema calcula el tiempo de preparación y confirma el pedido de la pizza.
Salir: Finaliza la sesión del usuario.

Requisitos
El proyecto no requiere dependencias externas. Solo necesitas tener Python instalado para ejecutar el programa.

Ejecución
Para ejecutar el programa, simplemente utiliza el siguiente comando en tu terminal o consola:

        python jat_v2.py

Explicación del Código
El código está estructurado en funciones para facilitar su comprensión, mantenimiento y posible ampliación futura. Se han incluido docstrings en todas las funciones para documentar su propósito, parámetros y valores de retorno.

¿Qué son los Docstrings?
Los docstrings son una forma de documentar el código en Python. Se escriben como un comentario dentro de las funciones y tienen el siguiente propósito:

Descripción de la Función: Proporcionan una breve descripción de lo que hace la función.
Parámetros: Describen los parámetros que la función acepta, incluyendo su tipo y su propósito.
Valor de Retorno: Explican qué valor devuelve la función, si es aplicable.

Ejemplo de Docstring

A continuación, se muestra un ejemplo de cómo se ha documentado una de las funciones en el código:

        def mostrar_menu():
            """
            Muestra el menú principal de opciones para el usuario.
            
            Opciones:
            1. Personalizar Pizza
            2. Ver Ingredientes
            3. Confirmar Pedido
            4. Salir
            """
            print("\n--- Menú de Pizza JAT ---")
            print("1. Personalizar Pizza")
            print("2. Ver Ingredientes")
            print("3. Confirmar Pedido")
            print("4. Salir")

Beneficios de los Docstrings

Claridad: Ayudan a otros desarrolladores (o a ti mismo en el futuro) a entender rápidamente qué hace cada parte del código.
Mantenimiento: Facilitan la actualización y corrección del código, ya que proporcionan una referencia clara de la intención original de cada función.

Documentación: Permiten que herramientas de documentación automática generen descripciones detalladas del código sin necesidad de escribir documentos separados.

Conclusión

Este proyecto es un ejemplo sencillo pero efectivo de cómo estructurar un programa en Python utilizando funciones bien documentadas. Los docstrings son una práctica recomendada que ayuda a mantener el código claro y fácil de entender.

