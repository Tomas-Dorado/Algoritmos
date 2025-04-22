from NodoClima import NodoClima

class ListaClima:
    def __init__(self):
        self.cabeza = None

    def agregar_clima(self, dia, clima):
        nuevo_nodo = NodoClima(dia, clima)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar_clima(self):
        actual = self.cabeza
        while actual:
            print(f"{actual.dia}: {actual.clima}")
            actual = actual.siguiente