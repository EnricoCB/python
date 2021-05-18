maior = total = cont = c = menorpreço = 0
while True:
    c += 1
    op = ''
    nome = input('Produto: ')
    preço = float(input('Preço: R$'))
    while True:
        if op == 'S' or op == 'N':
            break
        else:
            op = input('Você quer continuar? [S/N]: ').capitalize()
    if c == 1 or menorpreço > preço:
        menorpreço = preço
        menornome = nome
    if preço > 1000:
        cont += 1
    total += preço
    if op == 'N':
        break
print(f'O total gasto foi: {total}')
print(f'Produtos que custaram mais de R$1000: {cont}')
print(f'O produto mais caro foi {menornome} e custou: R${menorpreço}')