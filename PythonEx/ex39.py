from datetime import date
ano = int(input('Digite o seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - ano
if idade < 18:
    menor = 18 - idade
    print(f'Ainda não é hora de se alistar, faltam {menor} anos')
elif idade == 18:
    print('É hora de se alistar')
else:
    maior = idade - 18
    print(f'já passou do tempo do alistamento faz {maior} anos')