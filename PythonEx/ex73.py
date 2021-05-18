tabela = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense', 'Atlético-MG', 'Botafogo', 'Athletico-PR', 'Bahia', 'São paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
for pos, time in enumerate(tabela):
    print(f'{pos + 1}° {time}')

print(f'Os 5 primeiros times são {tabela [0:5]}')
print(f'Os 4 ultimos times são {tabela[-4:]}')
print(f'Os times em ordem alfabetica {sorted(tabela)}')
for c, time in enumerate(tabela):
    if time == 'Chapecoense':
        print(f'A Chapecoense esta em {c + 1}° lugar')