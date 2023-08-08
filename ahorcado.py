
errores = 0
maxErrores = 5
listaUbicaciones = []
ubicaciones = ""
continuar = True
    
while continuar == True:
    palabra = input("Elige una palabra: ").upper()
    errores = 0
    cadena = ""
    for l in palabra:
        cadena = cadena + "_"
    felicitaciones = "¡¡FELICITACIONES!! Acertaste la palabra {} con {} errores".format(palabra, errores)
    largo = len(palabra)
    
    while errores < 5:
        print(f"{cadena}, es una palabra de {largo} letras.")

        letra = input("Elige una letra: ").upper()
        if letra == palabra:
            print(felicitaciones)
            break
        if letra in palabra:
            for i, l in enumerate(palabra):
                if l == letra:
                    listaUbicaciones.append(i)
                    for i in listaUbicaciones:
                        cadena = cadena [0:i] + letra + cadena[i+1:]
                        listaUbicaciones = []
                        if ubicaciones == "":
                            ubicaciones = str(i+1)
                        else: ubicaciones = ubicaciones + ", " + str(i+1)
            if cadena == palabra:
                        print(felicitaciones)
                        break
            else:
                print(f"Bien! Acertaste la letra {letra}. Estaba en la posición {ubicaciones}.")
                ubicaciones = ""
            
        else:
            errores += 1
            intentosRestantes = maxErrores - errores
            if intentosRestantes > 1:
                print(f"La letra {letra} no está. Cuidado, te quedan {intentosRestantes} errores.")
            else:
                print("La letra no está. Cuidado, un error más y pierdes.")
            
    if errores == 5:
        print(f"""Perdiste. Te equivocaste {errores} veces y no lograste adivinar la palabra.
    La palabra era {palabra}.""")
    respuesta = input("¿Quieres jugar una vez más?: ")
    if respuesta.upper() == "NO":
        print("Ok, gracias por jugar!")
        continuar = False