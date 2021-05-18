from random import randint
def sorteio(lista):
    c = 0
    while c < 5:
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')
        c += 1


def somapar(lista):
    s = 0
    for c in range (0, 5):
        if lista[c] % 2 == 0:
            s += lista[c]
    print(f'\nSomando os valores pares de {lista} temos {s}')


numeros = []
sorteio(numeros)
somapar(numeros)