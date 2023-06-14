# Elección de Máquina
import random

num_rand = random.randint(1, 3)
if num_rand == 1:
    choice_maq= 'Piedra'
elif num_rand == 2:
    choice_maq= 'Papel'
else:
    choice_maq = 'Tijeras'
# Elección de Usuario
choice_text = '''
Escribe una Opción
    Piedra
    Papel
    Tijeras
'''
choice_user = input(choice_text)
# Imprime selección
print("Usuario elige: ", choice_user)
print("Máquina elige: ", choice_maq)

# Define ganador
if choice_user == choice_maq:
    print("Es un empate")
else:
    if choice_user == 'Piedra' and choice_maq == 'Papel':
        print("¡Gana Máquina!")
    elif choice_user == 'Piedra' and choice_maq == 'Tijeras':
        print("¡Gana Usuario!")
    elif choice_user == 'Papel' and choice_maq == 'Piedra':
        print("¡Gana Usuario!")
    elif choice_user == 'Papel' and choice_maq == 'Tijeras':
        print("¡Gana Máquina!")
    elif choice_user == 'Tijeras' and choice_maq == 'Piedra':
        print("¡Gana Máquina!")
    elif choice_user == 'Tijeras' and choice_maq == 'Papel':
        print("¡Gana Usuario")
    else: 
        print("¡Escribe bien, Usuario!")