import random


def generar_contraseña(longitud_b):
    longitud_a = 0
    clave = {1: [f'{random.randint(0,9)}'],
             2: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
             3: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
             4: ['¡', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', ',', '.', '<', '>', '¿', '?']}
    contraseña = []
    while longitud_a < longitud_b:
        tipo = random.randint(1, 4)
        contraseña.append(clave[tipo][random.randint(0, len(clave[tipo]) - 1)])
        longitud_a += 1
    return ''.join(contraseña)
longitud = int(input('Introduce la longitud de la contraseña: '))
print("Contraseña aleatoria con longitud "+str(longitud)+": "+generar_contraseña(longitud))
