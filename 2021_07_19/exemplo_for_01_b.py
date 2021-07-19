#escreva("Informe o Valor para Exibir a Tabuada de Multiplicação: ")
#leia(valor_entrada)

#para (inteiro multiplicador=1; multiplicador<=10; multiplicador++) {
#   escreva(valor_entrada, " | ", multiplicador, " | ", valor_entrada * multiplicador, "\n")
#}

#escreva("Fim da Tabuada")

valor_entrada = int(input('Informe o Valor para Exibir a Tabuada de Multiplicação: '))

if (valor_entrada != 0):
   for multiplicador in range(1, 11, 1):
      print(valor_entrada, ' | ', multiplicador, ' | ', valor_entrada * multiplicador)

print('Fim da Tabuada...')


# --------------------------------------------------------------
# Função RANGE()
# Sintaxe:  range(start, stop, step)
# start -> valor de início do range (opcional). Se omitido será atribuído o valor ZERO
# stop  -> valor de parada do range (obrigatório). O range irá parar no valor stop-1
# step  -> valor de incremento (opcional). Se omitido será atribuído o valor 1