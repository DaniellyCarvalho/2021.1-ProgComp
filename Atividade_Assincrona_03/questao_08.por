programa
{
	
	funcao inicio()
	{
		inteiro a, b, c
		escreva("Informe o valor do lado A: ")
		leia(a)
		escreva("Informe o valor do lado B: ")
		leia(b)
		escreva("Informe o valor do lado C: ")
		leia(c)
		se (a <= 0 ou b <= 0 ou c <= 0) {
			escreva("Foi informado um ângulo inválido")
		} senao {
			se (a >= b + c ou b >= a + c ou c >= a + b) {
				escreva("Os Lados Informados Não Formam um Triângulo")  
			} senao {
				se (a == b e b == c) {
					escreva("Triângulo EQUILÁTERO")	
				} senao {
					se (a != b e a != c e b!= c) {						
						escreva("Triângulo ESCALENO")	
					} senao {
						escreva("Triângulo ISÓSCELES")
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
 * @POSICAO-CURSOR = 500; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */