def ficha(nome="desconhecido", gols=0):
    if nome == '':
        nome = '<desconhecido>'
    if gols == ''  or not gols.isnumeric():
        gols = '0'
    print(f'O jogador {nome} marcou {gols}')



nome = input('Nome do jogador: ')

gols = (input('Número de gols: '))
ficha(nome, gols)