# emprendedor2.py
# Solicitar datos al usuario
P = float(input("Ingrese el precio de suscripción: "))
U_normal = int(input("Ingrese el número de usuarios normales: "))
U_premium = int(input("Ingrese el número de usuarios premium: "))
GT = float(input("Ingrese los gastos totales: "))

# Calcular utilidades
utilidades = (P * U_normal) + (P * 1.5 * U_premium) - GT

# resultado
print(f"Las utilidades del proyecto son {utilidades:.2f}")
