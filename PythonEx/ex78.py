valores = list()
for c in range (0,5):
    valores.append(int(input('Digite um valor: ')))
for pos, v in enumerate(valores):
    if pos == 0:
        maior = v
        menor = v
    if v > maior:
        maior = v
    if v < menor:
        menor = v
print(f'Você digitou os valores {valores}')
print(f'O maior valor é {maior} e esta na posição', end=' ')
for c in range (0, len(valores)):
    if maior == valores[c]:
        print(c, end=' ')

print(f'\nO menor valor é {menor} e esta na posição', end=' ')
for c in range (0, len(valores)):
    if menor == valores[c]:
        print(c, end=' ')
