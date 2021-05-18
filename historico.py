n = list()
r = list()
op = []
c = 0
c2 = 1
c3 = 0
opção = 'S'
while True:
    if c > 0:
        opção = str(input('Quer continuar? [S/N] ou ver historico [H]: ')).strip(' ').capitalize()
    if opção == 'S':
        op.append (input('digite a operação: '))
        n.append(int(input()))
        n.append(int(input(f'{n[c]} {op[c3]} ')))
        if op[c3] == '+':
            r.append(n[c] + n[c2])
        elif op[c3] == '-':
            r.append(n[c] - n[c2])
        elif op[c3] == '/':
            r.append(n[c] / n[c2])
        elif op[c3] == '*':
            r.append(n[c] * n[c2])
        elif op[c3] == '°':
            r.append(n[c] ** n[c2])
        print(r[c3])
        c += 2
        c2 += 2
        c3 += 1

    if opção == 'H':
        p1 = 0
        p2 = 1
        p3 = 0
        for p in range(0, len(op)):
            print(f'{n[p1]} {op[p3]} {n[p2]} = {r[p3]}')
            p1 += 2
            p2 += 2
            p3 += 1

    if opção == 'N':
        break
   