from datetime import date
menor = 0
maior = 0
anoatual = date.today().year
for c in range (1,8):
    idade = int(input('digite sua idade: '))
    idade = anoatual - idade
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} Pessoas são maiores de idade, e {menor} pessoas sao menores de idade')
