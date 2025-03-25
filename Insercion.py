def inserccion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

# Ejemplo de uso
if __name__ == "__main__":
    lista = [5, 2, 9, 1, 5, 6]
    print("Lista original:", lista)
    print("Lista ordenada:", inserccion(lista))