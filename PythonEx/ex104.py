def leiaInt(msg):
    n = input(msg)
    while True:
        if not n.isnumeric():
            print('\033[0;31mERRO! digite um número válido.\033[m')
            n = input(msg)
        else:
            n = int(n)
            break
    return n


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
