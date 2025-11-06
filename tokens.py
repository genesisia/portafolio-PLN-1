'''
tokens en python, especificamente lenguaje natural
se refiere ala dezcomposicion de un texto (oracion frase archivo de texto
con el objetivo de poder analizar el lenguaje escrito , por ejemplo
contar palabras contar longitud de las palabras descubrir el sentimiento plasmado
en el texto, traducirlo, etc.
'''
texto="hola, bienvenido al curso de Lenguaje natural con python "

#Limpieza basica
texto_Limpio=texto.replace(",","").replace(",","").lower()

#tokenizacion (separar por espacios)
tokens= texto_Limpio.split()
''' divide un texto en partes separadas por espacios (por defecto) y devuelve una lista de
palabras. cada palabra se convierte en un elemento de la lista'''

print("texto original",texto)
print("tokens",tokens)
print("Números de palabras ", len(tokens))