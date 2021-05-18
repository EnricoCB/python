def area():
    a = float(input('Largura (M): '))
    b = float(input('Comprimento (M): '))
    s = a * b
    print(f'A area de um terreno {a}x{b} é de {s}m².')


print('Area de terrenos')
print('-' * 30)
area()
