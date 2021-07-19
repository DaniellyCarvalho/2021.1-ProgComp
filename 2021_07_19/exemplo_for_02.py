#escreva("Informe um valor: ")
#leia(valor_x)
#soma_par = 0

#para(inteiro i=1; i <= valor_x; i++){
#   se(i % 2 == 0){
#      soma_par = soma_par + i
#   }
#}

#escreva(soma_par)

valor_x = int(input('Informe um valor: '))
soma_par = 0

for i in range(1, valor_x+1, 1):
   if (i % 2 == 0):
      soma_par += i
      print(i, ' | ', soma_par)

print('----------------')
print(soma_par)


# --------------------------------------------------------------
# Função RANGE()
# Sintaxe:  range(start, stop, step)
# start -> valor de início do range (opcional). Se omitido será atribuído o valor ZERO
# stop  -> valor de parada do range (obrigatório). O range irá parar no valor stop-1
# step  -> valor de incremento (opcional). Se omitido será atribuído o valor 1