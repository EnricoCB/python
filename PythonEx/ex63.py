termos = int(input('Quantos termos você quer mostrar? '))
c = 3
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end='')
while c <= termos:
    t3 = t1 + t2
    c += 1
    print(f' -> {t3}', end='')
    t1 = t2
    t2 = t3