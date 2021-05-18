sexo = str(input('Digite [M] para masculino e [F] para feminino: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, Digite [M] papa masculino e [F] para feminino: ')).strip().upper()[0]
