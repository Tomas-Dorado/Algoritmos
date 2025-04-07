from Polinomio import Polinomio

if __name__ == "__main__":
    # Primer polinomio
    p1 = Polinomio()
    p1.agregar_termino(3, 2)
    p1.agregar_termino(5, 0)
    p1.agregar_termino(2, 1)
    print("Polinomio 1:")
    p1.mostrar()  # Salida: 3x^2 2x^1 5x^0

    # Segundo polinomio
    p2 = Polinomio()
    p2.agregar_termino(1, 1)
    p2.agregar_termino(4, 0)
    print("Polinomio 2:")
    p2.mostrar()  # Salida: 1x^1 4x^0

    # Sumar los polinomios
    suma = p1.sumar(p2)
    print("Suma de Polinomio 1 y Polinomio 2:")
    suma.mostrar()  # Salida: 3x^2 3x^1 9x^0

    # Multiplicar los polinomios
    producto = p1.multiplicar(p2)
    print("Producto de Polinomio 1 y Polinomio 2:")
    producto.mostrar()  # Salida: 3x^3 11x^2 18x^1 20x^0