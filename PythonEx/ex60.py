numero = int(input('Digite um Número: '))
f = numero
c = numero - 1
while c != 0:
    f *= c
    c -= 1
print(f)