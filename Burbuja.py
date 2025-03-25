import time

def burbuja(lista:list):
    for i in range(0,len(lista)-1):
        for j in range(0,len(lista)-i-1):
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1]=lista[j+1], lista[j]
    return lista


if __name__ == "__main__":
    lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", lista)
    start_time = time.time()
    print("Lista ordenada:", burbuja(lista))
    end_time = time.time()
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")