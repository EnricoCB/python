n = list()
for c in range (0, 5):
    p = 0
    n.append(int(input('Digite um valor: ')))
    while p < c:
        if n[p] > n[c]:
            aux = n[p]
            n[p] = n[c]
            n[c] = aux
        p += 1
print(n)
        