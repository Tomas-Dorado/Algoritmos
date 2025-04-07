from Polinomio import Polinomio

if __name__ == "__main__":
    p = Polinomio()
    p.agregar_termino(3, 2)
    p.agregar_termino(5, 0)
    p.agregar_termino(2, 1)
    p.mostrar()  # Salida: 3x^2 2x^1 5x^0

    print(p.obtener_valor(1))  # Salida: 2
    print(p.existe_termino(2))  # Salida: True
    print(p.existe_termino(4))  # Salida: False

    p.eliminar_termino(1)
    p.mostrar()  # Salida: 3x^2 5x^0