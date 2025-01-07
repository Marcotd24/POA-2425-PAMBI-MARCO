#Hoy les traigo un programa para convertir metros a kilómetros
# Este programa toma una entrada en metros, la convierte a kilómetros y la muestra.

# Función para convertir metros a kilómetros
def convertir_a_kilometros(metros):
    """
    Convierte una longitud en metros a kilómetros.
    Argumentos:
    metros -- La longitud en metros a convertir.

    Retorna:
    La longitud convertida en kilómetros.
    """
    kilometros = metros / 1000.0  # Conversión de metros a kilómetros
    return kilometros


# Entrada del usuario: Longitud en metros
metros_usuario = float(input("Ingresa una longitud en metros: "))

# Verificar que la entrada es válida (mayor que 0)
if metros_usuario > 0:
    # Llamar a la función para la conversión
    kilometros = convertir_a_kilometros(metros_usuario)

    # Mostrar el resultado
    print(f"{metros_usuario} metros es igual a {kilometros} kilómetros.")
else:
    print("Por favor, ingresa un valor mayor a 0.")

