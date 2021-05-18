n1 = int(input('Digite tres numeros: \n'))
n2 = int(input(''))
n3 = int(input(''))
if n1 > n2 and n1 > n3:
    print(f'O maior numero é {n1}')
if n2 > n1 and n2 > n3:
    print(f'O maior numero é {n2}')
if n3 > n1 and n3 > n2:
    print(f'O maior numero é {n3}')
if n1 < n2 and n1 < n3:
    print(f'O menor numero é {n1}')
if n2 < n1 and n2 < n3:
    print(f'O menor valor é {n2}')
if n3 < n2 and n3 < n1:
    print(f'O menor valor é {n3}')
