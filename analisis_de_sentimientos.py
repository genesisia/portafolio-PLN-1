"""
crear una frase larga con palabras repetidos donde exprese un sentimiento positivo
y sentimientos negativos, analizar la frase completa, eliminando signos de puntuacion
, tokenizar la frase , y recorriente la frase con for, con if contabilizar cuanatas
palabras positivas y cuantas negativas se encontraran, y de ahi determinar
si la frase es positiva y negativa
"""
#funciones clave:replace,split,lower,for, if
#creando listas con las palabras para detectar el sentir de la frase
palabraspositivas=["feliz","contento","alegre","marravilloso","bonito","bonita"]
palabrasnegativas=["triste","solo","aburrida","malo","deprimido","horrible","muerto"]

frase="Hoy me siento triste, porque no pase la materia de Ecosistemas, porque mi compañero Angel, No me metio a su equipo, y valia el 40 porciento, pero aun asi me siento feliz porque ellos hayan pasado"

frase=frase.lower()
for signo in [",", ".", ";", ":", ",", ".", ".", ","]:
    frase = frase.replace(signo, "")

tokens=frase.split()

contador_positivas=0
contador_negativas=0

for palabra in tokens:
    if palabra in palabraspositivas:
        contador_positivas+=1
    elif palabra in palabrasnegativas:
        contador_negativas+=1

if contador_positivas > contador_negativas:
    sentimiento="La frase es POSITIVA"
elif contador_negativas > contador_positivas:
    sentimiento="La frase es NEGATIVA"
else:
    sentimiento="La frase es NEUTRA"

print("Tokens:", tokens)
print("Palabras positivas encontradas:", contador_positivas)
print("Palabras negativas encontradas:", contador_negativas)
print(sentimiento)