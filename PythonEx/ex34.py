s = float(input('Digite sue salário: '))
if s <= 1250.00:
    s = s * 1.15
else:
    s = s * 1.10
print(f'O salario agora é de {s:.2f}')