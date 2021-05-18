n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua outra nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print('Aprovado')
elif media < 7 and media >= 5:
    print('Recuperação')
else:
    print('reprovado')