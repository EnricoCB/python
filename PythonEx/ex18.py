import math
angulo = float(input('Digite um angulo: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print(f'O angulo {angulo} tem o seno de: {seno:.2f}')
print(f'O angulo {angulo} tem o cosseno de: {cos:.2f}')
print(f'O angulo {angulo} tem a tangente de: {tan:.2f}')