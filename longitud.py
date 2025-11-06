frase="mis lenjuages favoritos son: html ,php, python, pero se quedo con python."
tokens=frase.replace(",","").replace(":","").replace(".","").lower().split()
#['python','es','divertido','y','poderoso']

#crear una lista con las palabras verificadas
verificadas=[]#lista vacia donde se agregaron las palabras ya consultadas
#python,es,poderoso
for palabra in tokens: #python esta dentro de tokens
      if palabra not in verificadas:
        print(palabra,"tiene",len(palabra),"letras")
        verificadas.append(palabra)
        #python tiene 6 letras
        # es tiene 6 letras
        # es tiene 9 letras