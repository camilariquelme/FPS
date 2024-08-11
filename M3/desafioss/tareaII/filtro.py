def filtrar_productos(precios, umbral, condicion="mayor"):
    if condicion == "mayor":
        filtrados = {producto: precio for producto, precio in precios.items() if precio > umbral}
    elif condicion == "menor":
        filtrados = {producto: precio for producto, precio in precios.items() if precio < umbral}
    else:
        return "Lo sentimos, no es una operación válida"
    
    return filtrados

# Ejemplo de uso:
precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

print(filtrar_productos(precios, 30000))
print(filtrar_productos(precios, 30000, "menor"))
