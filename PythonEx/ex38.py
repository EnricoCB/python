n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print(f'O valor {n1} é maior que {n2}')
elif n2 > n1:
    print(f'O valor {n2} é maior que {n1}')
else:
    print(f'Os dois valores são iguais')