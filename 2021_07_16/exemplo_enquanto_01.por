programa
{
	
	funcao inicio()
	{
		inteiro valor_entrada
		inteiro multiplicador

		escreva("Informe o Valor para Exibir a Tabuada de Multiplicação: ")
		leia(valor_entrada)

		multiplicador = 1

		enquanto(multiplicador<=10){
			escreva(valor_entrada, " | ", multiplicador, " | ", valor_entrada * multiplicador, "\n")
			multiplicador = multiplicador + 1
		}

		escreva("Fim da Tabuada")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 361; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */