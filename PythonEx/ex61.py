primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
c = primeiro
while c < décimo + razão:
    print(f'{c}', end=' -> ')
    c += razão
print('acabou')
