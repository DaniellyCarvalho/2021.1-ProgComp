# Informando nome
nome = input('Informe o seu nome: ')

# Informando o ano de nascimento e convertendo para inteiro
ano_nascimento = int(input('Informe o ano do seu nascimento: '))

# Calculando a idade
idade = 2021 - ano_nascimento

# Imprimindo os valores
print('O seu nome é', nome)
print('Você tem', idade, 'anos')
print('Você nasceu em', ano_nascimento)

if idade >= 18:
   print('Você é MAIOR DE IDADE...')
   print('Você já pode tirar carteira de habilitação...')
else:
   print('Você é MENOR DE IDADE...')
