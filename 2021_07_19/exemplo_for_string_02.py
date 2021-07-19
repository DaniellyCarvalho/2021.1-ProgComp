texto = input('Informe um texto: ')

texto_invertido = ''

for letra in texto:
   texto_invertido = letra + texto_invertido

print(texto)
print(texto_invertido)

if (texto == texto_invertido):
   print('O texto é palíndromo')
else:
   print('O texto não é palíndromo')