n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
op = 1
while op != 5:
    op = int(input('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair\n'))
    if op == 1:
        r = n1 + n2
        print(f'{n1} + {n2} = {r}')
    elif op == 2:
        r = n1 * n2
        print(f'{n1} X {n2} = {r}')
    elif op == 3:
        if n1 > n2:
            r = n1
            print(f'Entre {n1} e {n2} o maior número é {r}')
        else:
            r = n2
            print(f'Entre {n1} e {n2} o maior número é {r}')
    elif op == 4:
        n1 = int(input('Digite o novo número: '))
        n2 = int(input('Digite o novo número: '))
    elif op == 5:
        print('Programa finalizado!')
    else:
        print('Opção invalida')
