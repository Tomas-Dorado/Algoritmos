def quicksort(arr):
    '''Quicksort recursivo que utiliza sublistas'''
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quicksort(left) + [pivot] + quicksort(right)

# Ejemplo de uso
if __name__ == "__main__":
    lista = [3, 6, 8, 10, 1, 2, 1]
    print("Lista original:", lista)
    lista_ordenada = quicksort(lista)
    print("Lista ordenada:", lista_ordenada)
