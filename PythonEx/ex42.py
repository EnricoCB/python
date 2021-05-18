a = float(input('Digite os lados A, B, C de um triangulo: \n'))
b = float(input())
c = float(input())
if a + b > c and a + c > b and b + c > a:
    if a == c and a == b and c == b:
        print('Pode formar um triangulo equilatero')
    elif a == c or a == b or c == b:
        print('Pode formar um triangulo isosceles')
    else:
        print('Pode formar um triangulo escaleno')
else:
    print('não pode formar um triangulo')