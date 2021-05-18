matriz = [[], [], []]
for c in range(0, 3):
    for l in range(0, 3):
        matriz[c].append(int(input()))

for c in range (0, 3):
    for l in range(0, 3):
        print(f'[{matriz[c][l]:^5}]', end='')
    print()

for l in range (0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            somaP += matriz[c][l]
        if c == 2:
            somaC += matriz[l][c]
        if l == 1:
            if m < matriz[l][c]:
                m = matriz[l][c]
print(f'A soma dos valores pares é {somaP}')
print(f'A soma dos valores da terceira coluna é de {somaC}')
print(f'o maior valor da segunda linha é {m}')