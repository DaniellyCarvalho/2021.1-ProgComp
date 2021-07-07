programa
{
	inclua biblioteca Matematica --> mat
	funcao inicio()
	{
		real a, b, c, delta, x1 , x2
		escreva("Informe o valor de A: ")
		leia (a)
		escreva("Informe o valor de B: ")
		leia (b)
		escreva("Informe o valor de C: ")
		leia (c)
		se (a != 0) {
			delta = mat.potencia(b, 2) - (4 * a * c)
			se (delta < 0) {
				escreva("Não Existem Raízes Reais")
			} senao {
				x1 = (- b + mat.raiz(delta, 2)) / (2 * a)
				se (delta == 0) {
					x2 = x1
				} senao {
					x2 = (- b - mat.raiz(delta, 2)) / (2 * a)
				}
				escreva ("A Raiz X1 é: ", x1, "\n")
				escreva ("A Raiz X2 é: ", x2)
			}
		} senao {
			escreva("Não é uma Equação do 2º Grau")
		}
	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 560; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */