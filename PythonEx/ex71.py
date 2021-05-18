valor = int(input('Qual o valor a ser sacado? R$'))
cinquenta = valor // 50
valor %= 50
vinte = valor // 20
valor %= 20
dez = valor // 10
valor %= 10
um = valor // 1
print(f'{cinquenta} Notas de R$50')
print(f'{vinte} Notas de R$20')
print(f'{dez} Notas de R$10')
print(f'{um} notas de R$1')