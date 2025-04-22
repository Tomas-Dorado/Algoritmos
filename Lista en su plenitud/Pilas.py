class NodoClima:
    def __init__(self, dia, clima):
        self.dia = dia
        self.clima = clima
        self.siguiente = None

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

class NodoCiudad:
    def __init__(self, ciudad, lista_clima):
        self.ciudad = ciudad
        self.lista_clima = lista_clima
        self.siguiente = None

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

# Ejemplo de uso
clima_bogota = ListaClima()
clima_bogota.agregar_clima("Lunes", "Soleado")
clima_bogota.agregar_clima("Martes", "Lluvioso")
clima_bogota.agregar_clima("Miércoles", "Nublado")
clima_bogota.agregar_clima("Jueves", "Soleado")
clima_bogota.agregar_clima("Viernes", "Lluvioso")
clima_bogota.agregar_clima("Sábado", "Nublado")
clima_bogota.agregar_clima("Domingo", "Soleado")

clima_medellin = ListaClima()
clima_medellin.agregar_clima("Lunes", "Nublado")
clima_medellin.agregar_clima("Martes", "Soleado")
clima_medellin.agregar_clima("Miércoles", "Soleado")
clima_medellin.agregar_clima("Jueves", "Lluvioso")
clima_medellin.agregar_clima("Viernes", "Nublado")
clima_medellin.agregar_clima("Sábado", "Soleado")
clima_medellin.agregar_clima("Domingo", "Lluvioso")

ciudades = ListaCiudades()
ciudades.agregar_ciudad("Bogotá", clima_bogota)
ciudades.agregar_ciudad("Medellín", clima_medellin)

ciudades.mostrar_ciudades()