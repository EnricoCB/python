v = float(input('Digite o valor da casa: R$'))
s = float(input('Digite o seu sálario: R$'))
a = int(input('Digite a quantidade de anos que vai querer pagar a casa: '))
e = v / (a*12)
ps = s * 0.30
if ps < e:
    print('Você não pode fazer este emprestimo')
else:
    print(f'O valor mensal a se pagar é R${e:.2f}') 
