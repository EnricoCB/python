n = int(input('Digite um número: '))
op = int(input('Digite 1 para binario / 2 para octal / 3 para hexadecimal: '))
if op == 1:
    print(f'{n} convertido para binario é {bin(n)[2:]}')
elif op == 2:
    print(f'{n} convertido para octal é {oct(n)[2:]}')
elif op == 3:
    print(f'{n} convertido para hexadecimal é {hex(n)[2:]}')
else:
    print('Opção invalida')
