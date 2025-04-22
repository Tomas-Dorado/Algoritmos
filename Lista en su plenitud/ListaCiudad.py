from NodoCiudad import NodoCiudad

class ListaCiudades:
    def __init__(self):
        self.cabeza = None

    def agregar_ciudad(self, ciudad, lista_clima):
        nuevo_nodo = NodoCiudad(ciudad, lista_clima)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar_ciudades(self):
        actual = self.cabeza
        while actual:
            print(f"Ciudad: {actual.ciudad}")
            actual.lista_clima.mostrar_clima()
            print()
            actual = actual.siguiente