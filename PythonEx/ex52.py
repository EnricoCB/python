n = int(input('Digite um numero: '))
tot = 0
for c in range (1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
if tot == 2:
    print(f'\nO número {n} é primo')
else:
    print(f'\nO número {n} não é primo')