def suma_lista(lista):
    if len(lista) == 0:
        return 0
    return lista[0] + suma_lista(lista[1:])


def contar_elementos(lista):
    if len(lista) == 0:
        return 0
    return 1 + contar_elementos(lista[1:])


# Programa principal
entrada = input("Escribe números separados por espacios: ")

# Convertimos el texto en una lista de números
numeros = list(map(int, entrada.split()))

print("Lista ingresada:", numeros)
print("Suma total:", suma_lista(numeros))
print("Cantidad de elementos:", contar_elementos(numeros))