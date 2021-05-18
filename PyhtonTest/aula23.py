try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'infelizmente tivemos um erro {erro.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('volte sempre, muito obrigado')