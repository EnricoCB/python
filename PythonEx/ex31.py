km = int(input('Informe a quantidade de KM: '))
if km <=200:
    p = km * 0.50
else:
    p = km * 0.45
print(f'O preço da viagem é de {p:.2f}')