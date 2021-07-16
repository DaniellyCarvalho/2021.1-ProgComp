programa
{
	
	funcao inicio()
	{
		inteiro valor_entrada

		escreva("Informe o Valor para Exibir a Tabuada de Multiplicação: ")
		leia(valor_entrada)

		para(inteiro multiplicador=1; multiplicador<=10; multiplicador++){
			escreva(valor_entrada, " | ", multiplicador, " | ", valor_entrada * multiplicador, "\n")
		}

		escreva("Fim da Tabuada")
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 186; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */