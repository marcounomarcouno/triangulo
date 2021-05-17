print("""
¡Hola!, con este programa podrás calcular el área de un triángulo.
Ingresa los datos que se te solicitan""")

altura = int(input('¿Cuál es la altura del triángulo?: '))
base = int(input('¿Cuál es la base del triángulo?: '))
area = (base * altura) / 2

print('El área de tu triángulo es: ' + str(area))

saber_tipo = """
¿Te gustaría conocer de qué tipo es tu triángulo? Sólo necesitas conocer la medida de sus lados.

Elige una opción:
1 = Sí
2 = No
"""

continuar = int(input(saber_tipo))

if continuar == 1:
    lado_a = int(input('¿Cuál es la medida del primer lado?: '))
    lado_b = int(input('¿Cuál es la medida del segundo lado?: '))
    
    if lado_a == lado_b and lado_a == base:
        print('Tu tiángulo es equilátero')
    elif lado_a != lado_b and lado_a == base:
        print('Tu triángulo es isósceles')
    elif lado_a == lado_b and lado_b != base:
        print('Tu triángulo es isósceles')
    elif lado_a != lado_b and lado_a != base:
        print('Tu triángulo es escaleno')

elif continuar == 2:
    print('De acuerdo. Nos vemos en a la próxima :) ')
else:
    print('Elige una opción válida')

