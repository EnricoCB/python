primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
c = primeiro
tot = 10
repetição = 1
while c < décimo + razão:
    print(f'{c}', end=' -> ')
    c += razão
print('Pausa')
while repetição != 0:
    repetição = int(input('quantos termos mais quer ver? '))
    décimo += razão * repetição
    tot += repetição
    while c <= décimo:
        print(f'{c}', end=' -> ')
        c += razão
    print('Pausa')
print(f'Foram mostrados {tot} termos')
