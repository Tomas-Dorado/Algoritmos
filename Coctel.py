import time

def coctel(lista):
    izquierda = 0
    derecha = len(lista) - 1
    control=True
    while izquierda<derecha and control:
        control=False
        for i in range(izquierda, derecha):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                control=True
        if not control:
            break
        control=False
        derecha -= 1
        for i in range(derecha, izquierda, -1):
            if lista[i - 1] > lista[i]:
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
                control=True
        izquierda
    return lista

if __name__ == "__main__":
    lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", lista)
    start_time = time.time()
    print("Lista ordenada:", coctel(lista))
    end_time = time.time()
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")