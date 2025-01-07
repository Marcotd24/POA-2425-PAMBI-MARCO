# Clase Hotel
class Hotel:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.habitaciones = []  # Lista de habitaciones

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_info(self):
        print(f"Hotel: {self.nombre}, Ubicación: {self.ubicacion}")
        print("Habitaciones disponibles:")
        for habitacion in self.habitaciones:
            print(f"- {habitacion.numero} - {habitacion.tipo}")

# Clase Habitacion
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.reservada = False

    def reservar(self):
        if not self.reservada:
            self.reservada = True
            print(f"Habitación {self.numero} reservada.")
        else:
            print(f"Habitación {self.numero} ya está reservada.")

    def liberar(self):
        self.reservada = False
        print(f"Habitación {self.numero} liberada.")

# Crear objetos
hotel = Hotel("Grand Plaza", "Madrid")
habitacion1 = Habitacion(101, "Individual", 50)
habitacion2 = Habitacion(102, "Doble", 80)

# Agregar habitaciones al hotel
hotel.agregar_habitacion(habitacion1)
hotel.agregar_habitacion(habitacion2)

# Mostrar información del hotel
hotel.mostrar_info()

# Reservar una habitación
habitacion1.reservar()

# Liberar una habitación
habitacion1.liberar()
