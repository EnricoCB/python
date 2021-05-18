def fatorial(numero, show=False):
    """-> Calcula o Fatorial de um numero

    Args:
        numero (int): O numero a ser calculado
        show (lógico, opcional): Mostrar ou nao a conta. Defaults to False.

    Returns: O valor do fatorial de um numero
    """
    f = 1
    for c in range (numero, 0, -1):
        if show == True:
            print(f'{c} X',end=' ')
        f *= c 
    return f
#numero = int(input('Informe o fatorial: '))
#print(f'= {fatorial(numero, True)}')
help (fatorial)