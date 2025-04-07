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

    def modificar_termino(self, termino, nuevo_valor):
        """Modifica el valor de un término existente en el polinomio."""
        actual = self.termino_mayor
        while actual is not None:
            if actual.dato.termino == termino:
                actual.dato.valor = nuevo_valor
                return True
            actual = actual.siguiente
        return False

    def mostrar(self):
        """Muestra el contenido del polinomio."""
        actual = self.termino_mayor
        polinomio_str = ""
        while actual is not None:
            signo = " + " if actual.dato.valor > 0 and polinomio_str else ""
            polinomio_str += f"{signo}{actual.dato.valor}x^{actual.dato.termino}"
            actual = actual.siguiente
        print(polinomio_str.strip())

    def sumar(self, otro_polinomio):
        """Suma el polinomio actual con otro polinomio."""
        resultado = Polinomio()
        actual = self.termino_mayor

        while actual is not None:
            resultado.agregar_termino(actual.dato.valor, actual.dato.termino)
            actual = actual.siguiente

        otro_actual = otro_polinomio.termino_mayor
        while otro_actual is not None:
            resultado.agregar_termino(otro_actual.dato.valor, otro_actual.dato.termino)
            otro_actual = otro_actual.siguiente

        return resultado

    def multiplicar(self, otro_polinomio):
        """Multiplica el polinomio actual con otro polinomio."""
        resultado = Polinomio()
        actual = self.termino_mayor

        while actual is not None:
            otro_actual = otro_polinomio.termino_mayor
            while otro_actual is not None:
                nuevo_valor = actual.dato.valor * otro_actual.dato.valor
                nuevo_termino = actual.dato.termino + otro_actual.dato.termino
                resultado.agregar_termino(nuevo_valor, nuevo_termino)
                otro_actual = otro_actual.siguiente
            actual = actual.siguiente

        return resultado