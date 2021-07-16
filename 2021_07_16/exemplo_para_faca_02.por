programa
{
	
	funcao inicio()
	{
		inteiro valor_x
		inteiro soma_par
		
		escreva("Informe um valor: ")
		leia(valor_x)

		soma_par = 0
		
		para(inteiro i=1; i <= valor_x; i++){
			se(i % 2 == 0){
				soma_par = soma_par + i
			}
		}

		escreva(soma_par)
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 203; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */