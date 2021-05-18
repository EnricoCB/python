n = (int(input('Informe um número: ')), int(input('Informe um número: ')), int(input('Informe um número: ')), int(input('Informe um número: ')), int(input('Informe um número: ')))
print(n)
cont = 0
for num in n:
    if num == 9:
        cont += 1
    if num == 3:
        print(f'A primeira posição que apareceu o numero 3: {n.index(3) + 1}')
    if num % 2 == 0:
        print(num, end=' ')
print(f'\nO número 9 foi digitado {cont} vezes')