import time

def seleccion(lista):
    for i in range(len(lista)):
        minimo = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista

if __name__ == "__main__":
    lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", lista)
    start_time = time.time()
    print("Lista ordenada:", seleccion(lista))
    end_time = time.time()
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
