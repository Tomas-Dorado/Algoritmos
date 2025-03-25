def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    # Mezclar las dos mitades ordenadas
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregar los elementos restantes
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

def mergesort(lista):
    if len(lista) <= 1:
        return lista

    # Dividir el array en dos mitades
    mitad = len(lista) // 2
    mitad_izquierda = mergesort(lista[:mitad])
    mitad_derecha = mergesort(lista[mitad:])

    # Mezclar las mitades ordenadas
    return merge(mitad_izquierda, mitad_derecha)

def ordenar_por_mezcla(lista):
    lista_ordenada = mergesort(lista)
    lista[:] = lista_ordenada  # Copiar los elementos ordenados de vuelta a la lista original

# Ejemplo de uso
if __name__ == "__main__":
    array = [38, 27, 43, 3, 9, 82, 10]
    print("Array original:", array)
    ordenar_por_mezcla(array)
    print("Array ordenado:", array)