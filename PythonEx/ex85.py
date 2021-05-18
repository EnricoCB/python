num = [[], []]
for c in range (0, 7):
    valor = int(input())
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
num[0].sort()
num[1].sort() 
print(num)
print(f'os numeros inpares foram {num[1]}')
print(f'Os valores pares foras {num[0]}')