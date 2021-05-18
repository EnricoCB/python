import random
from time import sleep
na = random.randint(1, 5)
n = int(input('Digite um numero: '))
print('PROCESSANDO...')
sleep(2)
if n == na:
    print('você acertou!')
else:
    print(f'você errou, o numero certo era {na}') 