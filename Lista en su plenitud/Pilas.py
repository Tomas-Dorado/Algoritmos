from ListaCiudad import ListaCiudades
from ListaClima import ListaClima

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