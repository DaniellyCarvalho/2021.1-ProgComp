# Informando nome
nome = input('Informe o seu nome: ')

# Informando a idade e já convertendo para inteiro
idade = int(input('Informe a sua idade: '))

# Calculando o ano de nascimento
ano_nascimento = 2021 - idade

# Imprimindo os valores
print('O seu nome é', nome)
print('Você tem', idade, 'anos')
print('Você nasceu em', ano_nascimento)

print('O seu nome é ' + nome + ' você nasceu em ' + str(ano_nascimento) + ' e tem ' + str(idade) + ' anos')