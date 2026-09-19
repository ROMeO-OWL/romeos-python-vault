from colorama import *
init()
def maximo_vocales_consonantes(vector):
    vocales = 'aeiou'
    palabra_maxima = ""
    contador_maximo = 0

    for palabra in vector:
        contador_vocales = 0 ; contador_consonantes = 0
        vocales_usadas = ""

        for letra in palabra:
            if letra in vocales:
                contador_vocales += 1
                if letra not in vocales_usadas:vocales_usadas += letra ; contador_consonantes += 1
            else: contador_consonantes += 1

        if contador_vocales > contador_maximo or (contador_vocales == contador_maximo and contador_consonantes > contador_consonantes):
            contador_maximo = contador_vocales
            palabra_maxima = palabra
    return palabra_maxima

vector = []
while True:
    palabra = input(Fore.CYAN+"Introduce una palabra o escribe 'Exit' para terminar:\n--> ").lower()
    if palabra == 'exit':print(Fore.RED+"Adios...") ; break
    vector.append(palabra)

palabra_max = maximo_vocales_consonantes(vector)
print(Fore.CYAN+"La palabra con la mayor cantidad de vocales y consonantes diferentes es: ", palabra_max)