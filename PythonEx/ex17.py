from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = hypot(ca, co)
print(f'O valor da hipotenuza é de: {h:.2f}')