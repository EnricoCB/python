op = 'S'
c = 0
m = 0
while op == 'S':
    c += 1
    n = int(input('Digite um número: '))
    m += n
    if c == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    op = str(input('Deseja adiciona mais algum número? [S/N]: ')).strip().upper()[0]
print(f'O maior número foi {maior} e o menor número foi {menor}\nA média é de {m/c}')

