pessoas = {}
lista = []
média = 0
op = ' '
while True:
    pessoas['nome'] = input('Nome: ')
    while True:
        pessoas['sexo'] = input('Sexo [M/F]: ').upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! digite M ou F')
    pessoas['idade'] = int(input('Idade: '))
    lista.append(pessoas.copy())
    while True:
        op = str(input('Quer continuar? [S/N]: ')).lower()
        if op in 'sn':
            break
        print('ERRO! digite apenas S ou N')
    if op == 'n':
        break
print('-=' * 30)

for c in range (0, len(lista)):
    média += lista[c]['idade']
média = média / len(lista)

print(f'- O grupo tem {len(lista)} pessoas')
print(f'- A média de idade do grupo é de {média:.2f} anos')
print('- as mulheres cadastradas foram:', end=' ')

for c in range(0, len(lista)):
    if lista[c]['sexo'] == 'F':
        print(f'{lista[c]["nome"]}', end='; ')

print('\nlistas de pessoas que a idade é maior que a média:')

for c in range(0, len(lista)):   
    if lista[c]['idade'] > média:
        print(f'nome = {lista[c]["nome"]}; sexo = {lista[c]["sexo"]}; idade = {lista[c]["idade"]}')
