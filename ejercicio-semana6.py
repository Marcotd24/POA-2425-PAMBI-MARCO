#Ejemplo de polimorfismo
#Clase base: Artista a nivel mundial

class Artista:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self._obras = []  # Atributo protegido para almacenar obras

    def agregar_obra(self, titulo):
        """Agrega una obra al repertorio del artista."""
        self._obras.append(titulo)

    def mostrar_obras(self):
        """Muestra todas las obras del artista."""
        return f"Obras de {self.nombre}: {', '.join(self._obras) if self._obras else 'No tiene obras registradas.'}"

    def mostrar_info(self):
        """Muestra información general del artista."""
        return f"Artista: {self.nombre}, Nacionalidad: {self.nacionalidad}"

# Clase derivada: Pintor
class Pintor(Artista):
    def __init__(self, nombre, nacionalidad, estilo):
        super().__init__(nombre, nacionalidad)
        self.estilo = estilo

    # Sobrescritura de método
    def mostrar_info(self):
        base_info = super().mostrar_info()
        return f"{base_info}, Estilo: {self.estilo}"

# Clase derivada: Escultor
class Escultor(Artista):
    def __init__(self, nombre, nacionalidad, material_favorito):
        super().__init__(nombre, nacionalidad)
        self.material_favorito = material_favorito

    # Sobrescritura de método
    def mostrar_info(self):
        base_info = super().mostrar_info()
        return f"{base_info}, Material favorito: {self.material_favorito}"

# Código principal
if __name__ == "__main__":
    # Crear instancias de artistas
    pintor = Pintor("Leonardo da Vinci", "Italiano", "Renacimiento")
    escultor = Escultor("Michelangelo", "Italiano", "Mármol")

    # Agregar obras
    pintor.agregar_obra("La Mona Lisa")
    pintor.agregar_obra("La última cena")
    escultor.agregar_obra("El David")
    escultor.agregar_obra("La Piedad")

    # Mostrar información y obras
    print(pintor.mostrar_info())
    print(pintor.mostrar_obras())

    print("\n" + escultor.mostrar_info())
    print(escultor.mostrar_obras())
