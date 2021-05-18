from time import sleep
def contagem(i, f, p):
    for c in range (1, 11, 1):
        print(c, end=' ', flush=True)
        sleep(0.5)
    print()
    for c in range (10, -1, -2):
        print(c, end=' ', flush=True)
        sleep(0.5)
    print()
    if p == 0:
        p = 1
    if p < 0:
        p *=  -1
    if i > f:
        for c in range(i, f - 1, -p):
            print(c, end=' ', flush=True)
            sleep(0.5)
    else:
        for c in range(i, f + 1, p):
            print(c, end=' ', flush=True)
            sleep(0.5)


a = int(input('Digite o inicio: '))
b = int(input('Digite o fim: '))
c = int(input('digite o passo: '))
contagem(a, b, c)