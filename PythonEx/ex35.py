a = float(input('Digite os lados a, b, c de um triangulo: \n'))
b = float(input(''))
c = float(input(''))
if a + b > c and a + c > b and c + b > a:
    print('Pode formar um triangulo!')
else:
    print('Não pode formar um triangulo')