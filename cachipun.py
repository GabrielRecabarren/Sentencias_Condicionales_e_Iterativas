import random
import sys

def jugar_cachipun(opcion_usuario):
    opciones = ['piedra', 'papel', 'tijera']
    
    if opcion_usuario not in opciones:
        print("Argumento inválido: Debe ser piedra, papel o tijera.")
        return
    #Random choice de la computadora para jugar contra ella
    opcion_computadora = random.choice(opciones)
    
    print("Tu jugaste:", opcion_usuario.capitalize())
    print("Computador jugó:", opcion_computadora.capitalize())
    #Casos según reglas del juego
    if opcion_usuario == opcion_computadora:
        print("Empate!")
    elif (opcion_usuario == 'piedra' and opcion_computadora == 'tijera') or \
         (opcion_usuario == 'papel' and opcion_computadora == 'piedra') or \
         (opcion_usuario == 'tijera' and opcion_computadora == 'papel'):
        print("Ganaste!!")
    else:
        print("Perdiste!")

# Obtener opción del usuario desde la línea de comandos
if len(sys.argv) != 2:
    print("Uso: python cachipun.py [piedra|papel|tijera]")
    sys.exit(1)

opcion_usuario = sys.argv[1].lower()

# Juegue!
jugar_cachipun(opcion_usuario)
