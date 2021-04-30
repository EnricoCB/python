from math import sqrt
op = input('Digite a operação: ')
n1 = float(input('Digite o numero: '))
if op == '_':
    r = sqrt(n1)
elif op == '°':
    r = n1 ** 2
else:
    n2 = float(input(f'{n1} {op} '))
    if op =='/':
        r = n1 / n2
    if op == '+':
        r = n1 + n2
    if op == '-':
        r = n1 - n2
    if op == '*':
        r = n1 * n2
while True:
    print(r)
    op = str(input('Quer continuar? [S/N]: ')).capitalize()
    if op == 'N':
        break
    op = input('Digite a operação: ')
    n = float(input(f'{r} {op} '))
    if op == '+':
        r = r + n
    if op =='/':
        r = n1 / n
    if op == '-':
        r = r - n
    if op == '*':
        r = r * n
print('O resultado final é: {}'.format(r))
