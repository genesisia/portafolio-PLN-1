from deep_translator import GoogleTranslator


def Traductor():
    texto = input("Ingresa el texto a traducir: ")
    print(f"\nTexto original: {texto}\n")

    while True:
        print("IDIOMAS DISPONIBLES")
        print("i  = Inglés")
        print("f  = Francés")
        print("a  = Alemán")
        print("it = Italiano")
        print("p  = Portugués")
        print("x  = Salir")

        idioma = input("\n¿A qué idioma deseas traducir? (Selecciona la opción): ").lower()

        if idioma == "i":
            ingles = GoogleTranslator(source='es', target='en').translate(texto)
            print(f"✓ Inglés: {ingles}\n")

        elif idioma == "f":
            frances = GoogleTranslator(source='es', target='fr').translate(texto)
            print(f"✓ Francés: {frances}\n")

        elif idioma == "a":
            aleman = GoogleTranslator(source='es', target='de').translate(texto)
            print(f"✓ Alemán: {aleman}\n")

        elif idioma == "it":
            italiano = GoogleTranslator(source='es', target='it').translate(texto)
            print(f"✓ Italiano: {italiano}\n")

        elif idioma == "p":
            portugues = GoogleTranslator(source='es', target='pt').translate(texto)
            print(f"✓ Portugués: {portugues}\n")


        elif idioma == "x":
            print("\n¡adios!")
            break

        else:
            print(" Error:Intenta de nuevo.\n")


Traductor()