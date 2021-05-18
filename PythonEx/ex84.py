maior = 0
menor = 0
p = list()
g = list()
while True:
    p.append(str(input('Informe seu nome: ')))
    p.append(float(input('Informe seu peso')))
    g.append(p[:])
    p.clear()
    for i in p:
        if i[1] > maior:
            maior = i[1]
    e = ''
    while e not in 'SN':
        e = str(input('Quer continuar? [S/N]')).capitalize()
    
    
    if e == 'N':
        break
