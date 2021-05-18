n = list()
c = 0
while True:
    p = 0
    op = ' '
    n.append(int(input('Digite um número: ')))
    while p < c:
        if n[p] == n [c]:
            del n[c]
            print('Valor DUPLICADO! não vou adicionar...')
            c -= 1
        p += 1
    while op not in 'SN':
       op = input('Quer continuar? [S/N]: ').capitalize()
    c += 1
    if op == 'N':
        break
print('-'*20)
n.sort()
print(f'Você digitou os valores {n}')
