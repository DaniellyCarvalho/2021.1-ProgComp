programa
{
	funcao inicio()
	{
		inteiro base, altura, area
		escreva("Informe o valor da BASE: ")
		leia (base)
		escreva("Informe o valor da ALTURA: ")
		leia (altura)
		se (base > 0 e altura > 0) {
			area = (base * altura) / 2
			escreva("A área do triângulo é: ", area)
		} senao {
			escreva("Dados Informados Inválidos!!!!")
		}
	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 218; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */