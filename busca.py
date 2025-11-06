frase = "Python es divertido y poderoso"
buscada = "python"

if buscada.lower() in frase.lower():
    print("La palabra está en la frase")
else:
    print("No se encontró la palabra")