from random import randint
c = randint(1, 10)
t = 1
n = int(input('Digite um número: '))
while n != c:
    n = int(input('Tente novamente: '))
    t += 1
print(f'Foram {t} tentativas para conseguir acertar o Número {c}')