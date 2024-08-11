from string import ascii_lowercase

def fuerza_bruta(password):
    intentos = 0
    for i, char in enumerate(password.lower()):
        for letra in ascii_lowercase:
            intentos += 1
            if letra == char:
                break
    return intentos

def main():
    password = input("Ingrese la contraseña: ")
    intentos = fuerza_bruta(password)
    print(f"La contraseña fue forzada en {intentos} intentos")

if __name__ == "__main__":
    main()