programa
{
	
	funcao inicio()
	{
		inteiro a, b, c
		escreva("Informe o valor do ângulo A: ")
		leia(a)
		escreva("Informe o valor do ângulo B: ")
		leia(b)
		escreva("Informe o valor do ângulo C: ")
		leia(c)
		se (a <= 0 ou b <= 0 ou c <= 0) {
			escreva("Foi informado um ângulo inválido")
		} senao {
			se (a + b + c != 180) {
				escreva("Os Ângulos Informados Não Formam um Triângulo")  
			} senao {
				se (a < 90 e b < 90 e c < 90) {
					escreva("Triângulo ACUTÂNGULO")	
				} senao {
					se (a == 90 ou b == 90 ou c == 90) {						
						escreva("Triângulo RETÂNGULO")	
					} senao {
						escreva("Triângulo OBTUSÂNGULO")
					}
				}
			}
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 632; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */