import sys 

def calcular_IMC(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC) dado el peso en Kg y la altura en metros.
    """
    imc = peso / (altura ** 2)
    return round(imc, 2)

def clasificar_IMC(imc):
    """
    Clasifica el IMC según la clasificación de la OMS.
    """
    if imc < 18.5:
        return "Bajo Peso"
    elif 18.5 <= imc < 25:
        return "Adecuado"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad Grado I"
    elif 35 <= imc < 40:
        return "Obesidad Grado II"
    else:
        return "Obesidad Grado III"

if __name__ == "__main__":
    # Verificar la cantidad de argumentos
    if len(sys.argv) != 3:
        print("Uso: python imc.py [peso_en_kg] [altura_en_cm]")
        sys.exit(1)

    # Obtener los argumentos de la línea de comandos
    try:
        peso = float(sys.argv[1])
        altura = float(sys.argv[2]) / 100  # Convertir altura de cm a metros
    except ValueError:
        print("Error: Los valores ingresados deben ser números.")
        sys.exit(1)

    # Cálculo del IMC
    imc = calcular_IMC(peso, altura)

    # Clasificación del IMC
    clasificacion = clasificar_IMC(imc)

    # Resultado
    print("Su IMC es:", imc)
    print("La clasificación OMS es:", clasificacion)
