valor = float(input('Qual é o valor do produto: '))
print ("""Qual a forma de pagamento
[1] A vista em dinheiro
[2] A vista no cartao
[3] até 2x no cartão
[4] 3x ou mais no cartão """)
op = int(input('Qual a opção de pagamento? '))
if op == 1:
    p = valor * 0.90
    print(f'O valor com 10% de desconto fica R${p}')
elif op == 2:
    p = valor * 0.95
    print(f'O valor com 5% de desconto fica R${p}')
elif op == 3:
    p = valor
    print(f'O valor não recebe desconto e fica R${p}')
elif op == 4:
    p = valor * 1.20
    print(f'O valor recebe 20% de juros e fica R${p}')
else:
    print('opção invalida')
