from random import randint
v = 0
d = 0
while True:
    nc = randint(0,20)
    e = str(input('Par ou Impar? ')).capitalize().strip()
    n = int(input('Qual número ira jogar? '))
    print('-'*35)
    print(f'Você jogou {n} e o computador jogou {nc}')
    if e == 'Par':
        if (nc + n) % 2 == 0:
            v += 1
            print(f'\033[1;32mVOCÊ GANHOU\033[m {nc} + {n} é igual a {nc + n} que é um número par')
        else:
            d = 1
    elif e == 'Impar':
        if (nc + n) % 2 == 1:
            v += 1
            print(f'\033[1;32mVOCÊ GANHOU\033[m {nc} + {n} é igual a {nc + n} que é um número impar')
        else:
            d = 1
    print('-'*35)
    if d == 1:
        print('\033[1;31mVOCÊ PERDEU\033[m')
        break
if v == 0:
    print('Você nao ganhou nenhuma vez')
elif v == 1:
    print('Você ganhou 1 vez')
else:
    print(f'Você ganhou {v} vezes')