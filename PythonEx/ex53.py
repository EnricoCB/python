frase = str(input('Digite a frase: ')).lower().strip()
frase = frase.split()
frase = "".join(frase)
fraseinvertida = frase[::-1]
if frase == fraseinvertida:
    print('é um palindromo')
else:
    print('não é um palindromo')
