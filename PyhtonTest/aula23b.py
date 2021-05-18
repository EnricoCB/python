try:
    a = int(input('Digite o numerador: '))
    b = int(input('digite o denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados')
else:
    print(f'O resultado é: {r:.1f}')
finally:
    print('Volte sempre, muito obrigado')