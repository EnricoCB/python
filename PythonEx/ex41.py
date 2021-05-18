from datetime import date
n = int(input('Digite sua idade: '))
anoatual = date.today().year
idade = anoatual - n
if idade <= 9:
    print('Mirin')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 20:
    print('Senior')
else:
    print('Master')