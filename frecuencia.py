#frase de ejemplo
frase="python es divertido y python es poderoso"

#1. limpiar el texto (minusculas y sin puntuacion basica)
frase_limpuar =frase.replace(",",",").lower()

#2 dividir en palabras (tokenizacion)
tokens=frase_limpuar.split()

#3. contar palabras usando un diccionario
frecuencia={}
for palabra in tokens:
    if palabra in tokens:
        frecuencia[palabra]+= 1
    else:
        frecuencia
