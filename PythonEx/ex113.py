def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            n = 0
            print('\n\033[0;31mO usuário preferiu não digitar o número.\033[m')
            break
        except Exception:
            print('\033[0;31mErro! Digite um número inteiro valido!\033[m')
        else:
            break
    return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (KeyboardInterrupt):
            print('\n\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número real valido!\033[m')
        else:
            return n


nInt = leiaInt('Digite um numero inteiro: ')
nFloat = leiaFloat('Digite um número real: ')
print(f'O numero inteiro que você digitou foi: {nInt}. O número real que você digitou foi: {nFloat}')