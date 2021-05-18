valores = list()
valores.append(5)
valores.append(4)
valores.append(9)

for c in range (2,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('cheguei ao final do programa') 