matriz = [[], [], []]
somaP = 0
somaC = 0
m = 0
for c in range (0, 3):
    for i in range (0, 3):
        matriz[c].append(int(input(f'O valor será adicionado na posição {[c]}{[i]}: '))) 

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

