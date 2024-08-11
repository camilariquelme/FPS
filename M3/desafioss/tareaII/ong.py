def factorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def productoria(lista):
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

def calcular(**kwargs):
    for clave, valor in kwargs.items():
        if 'fact' in clave:
            print(f"El factorial de {valor} es {factorial(valor)}")
        elif 'prod' in clave:
            print(f"La productoria de {valor} es {productoria(valor)}")

# Ejemplo de uso:
calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)
