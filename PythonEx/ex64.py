n = 0
t = 0
q = 0
while n != 999:
    n = int(input('Número: '))
    
    if n == 999:
        print('Programa finalizado')
    else:
        t += n
        q += 1
print(f'A quantidade de números digitados é de {q} e a soma deles é {t}')