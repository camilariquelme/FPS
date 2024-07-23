# Solicitar datos
P = float(input("Ingrese el precio de suscripción: "))
U = int(input("Ingrese el número de usuarios: "))
GT = float(input("Ingrese los gastos totales: "))

# Calcular utilidades
utilidades = P * U - GT

# Mostrar el resultado
print(f"Las utilidades del proyecto son {utilidades:.2f}")

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

# emprendedor3.py
# Solicitar datos al usuario
P = float(input("Ingrese el precio de suscripción: "))
U = int(input("Ingrese el número de usuarios normales: "))
GT = float(input("Ingrese los gastos totales: "))
U_anterior = float(input("Ingrese las utilidades del año anterior: "))

# Calcular utilidades actuales
U_actuales = P * U - GT

# Calcular razón de utilidades
razon = U_actuales / U_anterior

# Mostrar el resultado
print(f"Las utilidades actuales son {U_actuales:.2f}")
print(f"La razón entre las utilidades actuales y las del año anterior es {razon:.2f}")
