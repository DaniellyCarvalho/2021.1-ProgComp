#escreva("Informe o Valor para Exibir a Tabuada de Multiplicação: ")
#leia(valor_entrada)
#multiplicador = 1

#enquanto(multiplicador<=10){
#   escreva(valor_entrada, " | ", multiplicador, " | ", valor_entrada * multiplicador, "\n")
#   multiplicador = multiplicador + 1
#}

valor_entrada = int(input('Informe o Valor para Exibir a Tabuada de Multiplicação: '))
multiplicador = 1

while (multiplicador <= 10):
   print(valor_entrada, ' | ', multiplicador, ' | ', valor_entrada * multiplicador)
   #multiplicador = multiplicador + 1
   multiplicador += 1

print('Fim da Tabuada...')