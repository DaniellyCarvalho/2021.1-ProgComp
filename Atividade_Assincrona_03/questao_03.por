programa
{
	inclua biblioteca Matematica --> mat
	funcao inicio()
	{
		inteiro a, b, resultado
		escreva("Informe o valor de A: ")
		leia (a)
		escreva("Informe o valor de B: ")
		leia (b)
		resultado = mat.potencia(a, 2) + mat.potencia(b, 2)
		escreva("O resultado é: ", resultado)
	}
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 49; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */