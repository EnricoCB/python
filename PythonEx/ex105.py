def nota(*nota, sit=False):
    """Funcao para analisar n notas e retornar um dicionario com a maior nota, menor nota e media, com parametro opcional de mostrar a situação.

    Args:
        nota (float): armazena n notas.
        sit (bool, optional): indica se deve ou não mostrar a situação. Defaults to False.

    Returns:
        info: dicionario contendo informações sobre as notas
    """
    maior = 0
    menor = 0
    média = 0
    info = dict()
    for c in range (0, len(nota)):
        média += nota[c]
        if c == 0:
            maior = nota[c]
            menor = nota[c]
        else:
            if maior < nota[c]:
                maior = nota[c]   
            if menor > nota[c]:
                menor = nota[c]
    média = média / len(nota)
    info['total'] = len(nota)
    info['maior'] = maior
    info['menor'] = menor
    info['média'] = média
    if sit:
        if média < 4:
            info['Situação'] = 'ruim'
        elif média < 7:
            info['Situação'] = 'razoavel'
        else:
            info['Situação'] = 'Boa'
    return info

r = nota(5.5, 10, 9, 3, sit=True)
print(r)
