expressao = list()
c = 0
expressao.append(input('Digite a expressão: '))
for elemento in expressao:
    for i in elemento:
        if i == '(' or i ==')':
            c += 1
if c % 2 == 0:
    print('A expressão esta correta')
else:
    print('A expressão não esta correta')
