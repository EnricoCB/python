n = list()
c = e = 0
while True:
    c += 1
    n.append(int(input('Digite um número: ')))
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).upper()
    for num in n:
        if num == 5:
            e = 1
    if op == 'N':
        break
print(f'Foram digitados {c} numeros')
n.sort(reverse=True)
print(n)
if e == 1:
    print('O numero 5 esta na lista')
else:
    print('O numero 5 não esta na lista')