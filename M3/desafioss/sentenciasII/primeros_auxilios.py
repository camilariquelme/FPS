def primeros_auxilios():
    print("Bienvenido al sistema de primeros auxilios.")
    
    responde = input("¿Responde a estímulos? (s/n): ").lower()
    if responde == 's':
        print("Valorar la necesidad de llevarlo al hospital más cercano.")
        return
    
    print("Abrir la vía aérea")
    respira = input("¿Respira? (s/n): ").lower()
    if respira == 's':
        print("Permitirle posición de suficiente respiración")
        return
    
    print("Administrar 5 ventilaciones y llamar a ambulancia")
    
    while True:
        signos = input("¿Tiene signos de vida? (s/n): ").lower()
        if signos == 's':
            print("Reevaluar a la espera de la ambulancia")
            return
        
        print("Administrar compresiones torácicas hasta que llegue la ambulancia")
        
        ambulancia = input("¿Llegó la ambulancia? (s/n): ").lower()
        if ambulancia == 's':
            print("Transferir la atención a los profesionales")
            return

if __name__ == "__main__":
    primeros_auxilios()