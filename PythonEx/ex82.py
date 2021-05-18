n = list()
i = list()
p = list()
while True:
    n.append(int(input('Digite um número: ')))
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).capitalize()
    if op == 'N':
        break
for c in range (len(n)):
    if n[c] % 2 == 0:
        p.append(n[c])
    else:
        i.append(n[c])
print(n)
print(p)
print(i)
