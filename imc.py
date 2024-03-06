def calcular_IMC(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC) dado el peso en Kg y la altura en metros.
    """
    imc = peso / (altura ** 2)
    return round(imc,2)

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

# Entrada de datos
peso = float(input("Ingrese el peso en Kg: "))
altura_cm = float(input("Ingrese la altura en Centímetros: "))
altura=altura_cm/100

# Cálculo del IMC
imc = calcular_IMC(peso, altura)

# Clasificación del IMC
clasificacion = clasificar_IMC(imc)

# Resultado
print("El IMC es:", imc)
print("Clasificación OMS:", clasificacion)
