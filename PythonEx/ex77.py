palavras = ('aprender', 'programar', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado')
for p in palavras:
    print(f'\nna palavra {p} temos ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
