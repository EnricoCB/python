produtos = ('Monitor', 1400, 'Teclado', 160, 'Mouse', 200, 'Headset', 200, 'Computador', 5000, 'Mousepad', 100)
print('-'*30)
print('{:^30}'.format('lista de Compras'))
print('-'*30)

for c in range (0, len(produtos), 2):
    print(f'{produtos[c]:.<20}',f'R${produtos[c+1]:>7.2f}')
print('-'*30)
