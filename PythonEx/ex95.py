jogador = {}
lista = []
partidas = []
while True:
    jogador['nome'] = input('nome do jogador: ')
    qntd = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for c in range(0, qntd):
        partidas.append(int(input(f'Quantos gols na partida {c + 1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    partidas.clear()
    lista.append(jogador.copy())
    op = str(input('quer continuar? [S/N]: ')).capitalize()
    if op == 'N':
        break

print('-=' * 30)
print(f'{"cod nome":<15}     {"gols":<10}    {"total":>10}')
print('-=' * 30)

for c in range(0, len(lista)):
    print(f'{c + 1} {lista[c]["nome"]!s:<15s}  {lista[c]["gols"]!s:<19s}  {lista[c]["total"]!s:<15s}')

while True:
    op = int(input('Mostrar dados de qual jogador [999 para parar]: '))
    print('-=' * 30)
    if op == 999:
        break
    op -= 1
    if op <= len(lista) - 1 and op > -1:
        
        print(f'levantamento do jogador {lista[op]["nome"]}')
        for i, v in enumerate (lista[op]['gols']):
            print(f'no jogo {i + 1} fez {v} gols')
    else:
        print(f'ERRO! não existe jogador com código {op + 1}! tente novamente')
    print('-=' * 30)
