primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
décimo = primeiro + (10 - 1) * razao
for c in range (primeiro, décimo + razao, razao):
    print(f'{c}', end=' -> ')
print('acabou')