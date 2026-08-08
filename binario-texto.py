#Convertidor binario a texto(Nombres) y viceversa

res = input("Ingrese 1 para convertir de binario a texto o 2 para convertir de texto a binario: ")
numero_completo = ""
if res == "1":
    binario = input("Ingrese el número binario: ")
    for numero in range(0, len(binario), 8):
        byte = binario[numero:numero+8]
        decimal = int(byte, 2)
        letra = chr(decimal)
        print(f"El número binario '{byte}' es el numero '{decimal}' y en texto es '{letra}'")
else:
    if res == "2":
        texto = input("Ingrese el texto: ")
        for letra in texto:
            decimal = ord(letra)
            binario = format(decimal, '08b')
            print(f"La letra '{letra}' es el numero '{decimal}' y en binario es '{binario}'")
            numero_completo += binario
        print("El texto completo en binario es: ", numero_completo)