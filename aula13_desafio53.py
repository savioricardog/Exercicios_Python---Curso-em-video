#prog que leia uma frase qualquer e diga se é um palindromo

frase = str(input('Diga uma frase ').strip()).upper()
palavras = frase.split()
junto= ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('Não é um palindromo!')