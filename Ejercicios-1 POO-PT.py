# Comparación de Programación Tradicional y POO en Python
# Programación Tradicional

def obtener_humedades():
    """Solicita al usuario los niveles de humedad diarios y los almacena en una lista."""
    humedades = []
    for i in range(7):
        humedad = float(input(f"Ingresa el nivel de humedad del día {i + 1} (%): "))
        humedades.append(humedad)
    return humedades

def calcular_promedio_humedad(humedades):
    """Calcula el promedio de una lista de niveles de humedad."""
    return sum(humedades) / len(humedades)

def main_tradicional():
    """Función principal para la solución tradicional."""
    print("Programación Tradicional")
    humedades = obtener_humedades()
    promedio = calcular_promedio_humedad(humedades)
    print(f"El promedio semanal de humedad es: {promedio:.2f}%")

main_tradicional()

# Solución utilizando Programación Orientada a Objetos (POO)

class HumedadSemanal:
    """Clase que representa los niveles de humedad de una semana."""

    def __init__(self):
        """Inicializa la lista de niveles de humedad."""
        self.humedades = []

    def ingresar_humedad(self, humedad):
        """Agrega un nivel de humedad diario a la lista."""
        self.humedades.append(humedad)

    def calcular_promedio_humedad(self):
        """Calcula el promedio de los niveles de humedad semanales."""
        if not self.humedades:
            raise ValueError("No se han ingresado niveles de humedad.")
        return sum(self.humedades) / len(self.humedades)

def main_poo():
    """Función principal para la solución POO."""
    print("\nProgramación Orientada a Objetos (POO)")
    humedad = HumedadSemanal()

    for i in range(7):
        humedad_diaria = float(input(f"Ingresa el nivel de humedad del día {i + 1} (%): "))
        humedad.ingresar_humedad(humedad_diaria)

    promedio = humedad.calcular_promedio_humedad()
    print(f"El promedio semanal de humedad es: {promedio:.2f}%")

main_poo()

