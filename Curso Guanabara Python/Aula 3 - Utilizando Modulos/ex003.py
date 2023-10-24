from math import sin, cos, tan, radians

angulo = float(input('Digite o angulo: '))
angulo = radians(angulo)
print(f'O valor do Seno é: {sin(angulo):.2f}\nO valor de cosseno é: {cos(angulo):.2f}\nO valor do tangente é: {tan(angulo):.2f}')
