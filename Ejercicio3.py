from io import open_code


archivo = open ("archivo1.txt" , "a")
anotes = str (input("Ingresa una frase: "))
archivo.write (anotes)
archivo.close()
texto = open ("archivo1.txt" , "r")
print(texto.read())
archivo.close()