from Nodo import Nodo
from datoPolinomio import DatoPolinomio

class Polinomio:
    def __init__(self):
        self.grado = -1  # Grado del polinomio
        self.termino_mayor = None  # Puntero al término de mayor grado

    def agregar_termino(self, valor, termino):
        """Agrega un término al polinomio."""
        nuevo_dato = DatoPolinomio(valor, termino)
        nuevo_nodo = Nodo(nuevo_dato)

        if self.termino_mayor is None or termino > self.grado:
            nuevo_nodo.siguiente = self.termino_mayor
            self.termino_mayor = nuevo_nodo
            self.grado = termino
        else:
            actual = self.termino_mayor
            anterior = None
            while actual is not None and actual.dato.termino > termino:
                anterior = actual
                actual = actual.siguiente

            if actual is not None and actual.dato.termino == termino:
                actual.dato.valor += valor
            else:
                nuevo_nodo.siguiente = actual
                if anterior is None:
                    self.termino_mayor = nuevo_nodo
                else:
                    anterior.siguiente = nuevo_nodo

    def obtener_valor(self, termino):
        """Obtiene el valor del coeficiente de un término específico."""
        actual = self.termino_mayor
        while actual is not None:
            if actual.dato.termino == termino:
                return actual.dato.valor
            actual = actual.siguiente
        return 0

    def eliminar_termino(self, termino):
        """Elimina un término del polinomio."""
        actual = self.termino_mayor
        anterior = None
        while actual is not None and actual.dato.termino != termino:
            anterior = actual
            actual = actual.siguiente

        if actual is not None:
            if anterior is None:
                self.termino_mayor = actual.siguiente
            else:
                anterior.siguiente = actual.siguiente
            if termino == self.grado:
                self.grado = self.termino_mayor.dato.termino if self.termino_mayor else -1

    def existe_termino(self, termino):
        """Determina si un término existe en el polinomio."""
        actual = self.termino_mayor
        while actual is not None:
            if actual.dato.termino == termino:
                return True
            actual = actual.siguiente
        return False

    def mostrar(self):
        """Muestra el contenido del polinomio."""
        actual = self.termino_mayor
        polinomio_str = ""
        while actual is not None:
            polinomio_str += f"{actual.dato.valor}x^{actual.dato.termino} "
            actual = actual.siguiente
        print(polinomio_str.strip())