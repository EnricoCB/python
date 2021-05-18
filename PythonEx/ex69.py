maior = h = menor = 0
while True:
    sexo = opção = ''
    print('-' * 10)
    idade = int(input('Idade: '))
    while True:
        if sexo == 'M' or sexo == 'F':
            break
        else:
            sexo = input('Sexo [M/F]: ').capitalize()
    print('-' * 10)
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N]: ')).capitalize()
    if sexo == 'M':
        h += 1
    if idade > 18:
        maior += 1
    if sexo == 'F':
        if idade < 20:
            menor += 1
    if opção == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {h} homens cadastrados')
print(f'E temos {menor} mulheres com menos de 20 anos')