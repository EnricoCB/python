a = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(a)}')
print(f'É um numero? {a.isnumeric()}')
print(f'Só tem espaço? {a.isspace()}')
print(f'Está em maiuscula? {a.isupper()}')
print(f'Está em minuscula? {a.islower()}')
print(f'É alfabetico? {a.isalpha()}')
print(f'É alfanumerico? {a.isalnum()}')
print(f'Está capitalizada? {a.istitle()}')