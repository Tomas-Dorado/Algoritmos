import time

def burbuja_mejorada(lista):
    n = len(lista)
    i = 0
    while i < n:
        # Bandera para verificar si hubo intercambio
        intercambio = False
        j = 0
        while j < n - i - 1:
            if lista[j] > lista[j + 1]:
                # Intercambiar si el elemento es mayor que el siguiente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
            j += 1
        # Si no hubo intercambio, la lista ya está ordenada
        if not intercambio:
            break
        i += 1
    return lista

# Ejemplo de uso
if __name__ == "__main__":
    lista = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", lista)
    start_time = time.time()
    print("Lista ordenada:", burbuja_mejorada(lista))
    end_time = time.time()
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")