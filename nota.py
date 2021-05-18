materias = ['Português', 'Geografia', 'Ciências', 'Matematica', 'Historia']
b1 = []
b2 = []
m = []
for c in range(0, len(materias)):
    b1.append(float(input(f'Digite a nota de {materias[c]} do 1° bimestre: ')))

for c in range(0, len(materias)):
    b2.append(float(input(f'Digite a nota de {materias[c]} do 2° bimestre: ')))

for c in range(len(materias)):
    m.append((b1[c] + b2[c]) / 2)
    print(f'Sua média em {materias[c]} foi de: {m[c]}')
