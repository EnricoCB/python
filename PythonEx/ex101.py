def voto(idade):
    from datetime import date
    global i
    ano = date.today().year
    idade = ano - idade
    i = idade
    if idade < 16:
        voto = 'Não pode votar'
    elif idade < 18 or idade >= 70:
        voto = 'voto opcional'
    else:
        voto = 'voto obrigatorio'
    return voto


i = int(input('em que ano você nasceu: '))
v = voto(i)
print(f'idade: {i}; {v}.')