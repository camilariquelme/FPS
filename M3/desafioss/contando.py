import math

# Solicitar datos
r = float(input("Ingrese el radio en Kilómetros: ")) * 1000  # Convertir a metros
g = float(input("Ingrese la constante g: "))

# Calculo
Ve = math.sqrt(2 * g * r)

# Resultado
print(f"La velocidad de Escape es {Ve} [m/s]")
