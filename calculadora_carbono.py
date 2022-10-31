def calculadora_carbono():

	coeficientes = {
		'1' : 0.00407,
		'2' : 0.00468,
		'3' : 0.00084,
		'4' : 0.0022755}

	escrever_mensagem_boas_vindas()
	quantidade_carbono_primeiro_ano = 0
	quantidade_carbono_segundo_ano = 0

	resposta_primeira = str(input('Está tudo pronto para realização do calculo?(S/N) '))
	resposta_primeira = resposta_primeira.lower()

	if resposta_primeira == 'n':
		print('Calculadora encerrada.')

	elif resposta_primeira == 's':
		print('Agora, responda com os valores referentes ao primeiro ano da comparação.')
		quantidade_carbono_primeiro_ano += calculo(coeficientes)
		print(quantidade_carbono_primeiro_ano)

		while True:
			try:
				resposta_segunda = str(input('Deseja adicionar mais algum consumo nesse respectivo ano?(S/N) '))
				resposta_segunda = resposta_segunda.lower()

				if (resposta_segunda == 's'):
					quantidade_carbono_primeiro_ano += calculo(coeficientes)
					print(quantidade_carbono_primeiro_ano)

				elif (resposta_segunda == 'n'):
					break
				else:
					print('Resposta invalida, responda com S(sim) ou N(não)')

			except:
				print('Resposta invalida, responda com S(sim) ou N(não)')


		print('Agora, responda com os valores referentes ao segundo ano da comparação.')
		quantidade_carbono_segundo_ano += calculo(coeficientes)
		print(quantidade_carbono_segundo_ano)

		while True:
			try:
				resposta_segunda = str(input('Deseja adicionar mais algum consumo nesse respectivo ano?(S/N) '))
				resposta_segunda = resposta_segunda.lower()

				if (resposta_segunda == 's'):
					quantidade_carbono_segundo_ano += calculo(coeficientes)
					print(quantidade_carbono_segundo_ano)

				elif (resposta_segunda == 'n'):
					break

				else:
					print('Resposta invalida, responda com S(sim) ou N(não)')

			except:
				print('Resposta invalida, responda com S(sim) ou N(não)')
				


		diferenca = quantidade_carbono_primeiro_ano - quantidade_carbono_segundo_ano

		if diferenca > 0:
			print(f'Parabéns! Você adquiriu {diferenca:0.2f} créditos de carbono.')

		elif diferenca == 0:
			print(f'Seu consumo foi igual nos dois anos! Logo, você não adquiriu nenhum créditos de carbono.')

		else:
			print(f'Infelizmente, você aumento suas emissões de carbono de uma ano para o outro!')
			diferenca = abs(diferenca)
			print(f'Portanto, você deve comprar {diferenca:0.2f} créditos de carbono para compensar seu gasto a mais.')

	else:
		print('resposta inválida!')
		print('Calculadora encerrada.')


def escrever_mensagem_boas_vindas():
	print('************************************************')
	print('*Bem-vindo a calculadora de crédito de carbono!*')
	print('************************************************')

def calculo(coeficientes):

	while True:
		try:
			valor_quilometro = float(input('Digite a quantidade de quilômetros rodados por um tipo de veículo: '))
			break
		except:
			print('Resposta invalida, por favor, digite somente números!')	


	print('Tipos de combustivel: 1- Gasolina; 2 - Diesel; 3 - Eletrico; 4 - Etanol')
	while True:
		try:
			tipo_combustivel = str(input('Digite o tipo de combustivel (1/2/3/4): '))

			verficacao1 =  tipo_combustivel == '1'
			verficacao2 =  tipo_combustivel == '2'
			verficacao3 =  tipo_combustivel == '3'
			verficacao4 =  tipo_combustivel == '4'
			if verficacao1 or verficacao2 or verficacao3 or verficacao4:
				break
			else:
				print('Resposta invalida, digite apenas números (1/2/3/4).')

		except:
			print('Resposta invalida, por favor, digite somente números!')	

	while True:
		try:
			valor_consumo_gasolina = float(input('Digite o consumo do respectivel combustivel (l/100km): '))
			break

		except:
			print('Resposta invalida, por favor, digite somente números!')	


	coeficiente = coeficientes.get(tipo_combustivel)

	quantidade_carbono = valor_quilometro * (coeficiente) * (valor_consumo_gasolina / 100)

	return quantidade_carbono

if (__name__ ==	 '__main__'):
	calculadora_carbono()