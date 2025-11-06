numeros = [1, 2, 3, 4, 5]

for num in numeros:
    print(num)

#########################
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print("Me gusta la", fruta)

#########################
for i in range(5): # va de 0 a 4
    print("Número:", i)

#########################
palabra = "Python"

for letra in palabra:
    print(letra)

#########################
texto_limpio = "Hola mundo esto es python"
tokens = texto_limpio.split()

for token in tokens:
    print("Token:", token)