programa
{
	
	funcao inicio()
	{
		inteiro valor_x
		inteiro soma_par
		
		escreva("Informe um valor: ")
		leia(valor_x)

		soma_par = 0
		
		enquanto (valor_x != 0){
			se(valor_x % 2 == 0){
				soma_par = soma_par + valor_x
			}
			escreva("Informe um valor: ")
			leia(valor_x)				
		}

		escreva(soma_par)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 322; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */