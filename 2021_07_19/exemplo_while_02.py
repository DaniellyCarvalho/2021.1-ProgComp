#escreva("Informe um valor: ")
#leia(valor_x)
#soma_par = 0
#enquanto (valor_x != 0){
#   se(valor_x % 2 == 0){
#      soma_par = soma_par + valor_x
#   }
#   escreva("Informe um valor: ")
#   leia(valor_x)				
#}
#escreva(soma_par)

valor_x = int(input('Informe um valor: '))
soma_par = 0
while (valor_x != 0):
   if (valor_x % 2 == 0):
      #soma_par = soma_par + valor_x
      soma_par += valor_x
   valor_x = int(input('Informe um valor: '))
print(soma_par)