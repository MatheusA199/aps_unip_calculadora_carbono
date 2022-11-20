def calculadora_carbono():

	coeficientes = {
		'1' : 0.00407,
		'2' : 0.00468,
		'3' : 0.00084,
		'4' : 0.0022755}

	escrever_mensagem_boas_vindas()
	linha_vazia()
	quantidade_carbono_primeiro_ano = 0
	quantidade_carbono_segundo_ano = 0

	resposta_primeira = str(input('Está tudo pronto para realização do cálculo?(S/N) '))
	linha_vazia()
	resposta_primeira = resposta_primeira.lower()

	if resposta_primeira == 'n':
		print('Calculadora encerrada.')

	elif resposta_primeira == 's':
		print('Agora, responda com os valores referentes ao primeiro ano da comparação.')
		linha_vazia()
		quantidade_carbono_primeiro_ano += calculo(coeficientes)
		linha_vazia()
		while True:
			try:
				resposta_segunda = str(input('Deseja adicionar mais algum consumo nesse primeiro ano?(S/N) '))
				linha_vazia()
				resposta_segunda = resposta_segunda.lower()

				if (resposta_segunda == 's'):
					quantidade_carbono_primeiro_ano += calculo(coeficientes)

				elif (resposta_segunda == 'n'):
					break
				else:
					print('Resposta inválida, responda com S(sim) ou N(não)')

			except:
				print('Resposta inválida, responda com S(sim) ou N(não)')

		print('Agora, responda com os valores referentes ao segundo ano da comparação.')
		quantidade_carbono_segundo_ano += calculo(coeficientes)

		while True:
			try:
				resposta_segunda = str(input('Deseja adicionar mais algum consumo nesse segundo ano?(S/N) '))
				linha_vazia()
				resposta_segunda = resposta_segunda.lower()

				if (resposta_segunda == 's'):
					quantidade_carbono_segundo_ano += calculo(coeficientes)

				elif (resposta_segunda == 'n'):
					break

				else:
					print('Resposta inválida, responda com S(sim) ou N(não)')

			except:
				print('Resposta inválida, responda com S(sim) ou N(não)')

		diferenca = quantidade_carbono_primeiro_ano - quantidade_carbono_segundo_ano

		valor_credito_carbono = float(89.05)

		valor_em_reais = (valor_credito_carbono * diferenca)

		if diferenca > 0:
			print(f'Parabéns! Você adquiriu {diferenca:0.2f} créditos de carbono.')
			print(f'Com isso, você receberá {valor_em_reais:0.2f} reais na venda desses créditos! ')
		elif diferenca == 0:
			print(f'Seu consumo foi igual nos dois anos! Logo, você não adquiriu nenhum crédito de carbono.')

		else:
			diferenca = abs(diferenca)
			print(f'Infelizmente, você aumentou suas emissões de carbono de uma ano para o outro em {diferenca:0.2f}!')
			print(f'Portanto, para compensar o aumento de emissões, você deve comprar {diferenca:0.2f} créditos de carbono!')
			print(f'Para isso, você deverá desenbolsar {valor_em_reais:0.2f} reais.')

	else:
		print('Resposta inválida!')
		print('Calculadora encerrada.')


def escrever_mensagem_boas_vindas():
	print('************************************************')
	print('*Bem-vindo a calculadora de crédito de carbono!*')
	print('************************************************')

def calculo(coeficientes):

	while True:
		try:
			valor_quilometro = float(input('Digite a quantidade de quilômetros rodados por um tipo de veículo (Km): '))
			linha_vazia()
			break
		except:
			print('Resposta inválida, por favor, digite somente números!')	
			linha_vazia()

	print('Tipos de combustivel: 1- Gasolina; 2 - Diesel; 3 - Eletrico; 4 - Etanol')
	linha_vazia()
	while True:
		try:
			tipo_combustivel = str(input('Digite o tipo de combustivel (1/2/3/4): '))
			linha_vazia()

			verificacao1 =  tipo_combustivel == '1'
			verificacao2 =  tipo_combustivel == '2'
			verificacao3 =  tipo_combustivel == '3'
			verificacao4 =  tipo_combustivel == '4'
			if verificacao1 or verificacao2 or verificacao3 or verificacao4:
				break
			else:
				print('Resposta inválida, digite apenas os números (1/2/3/4).')

		except:
			print('Resposta inválida, por favor, digite somente números!')	
			linha_vazia()

	while True:
		try:
			if (verificacao3):
				valor_consumo_combustivel = float(input('Digite o consumo do respectivel combustivel (Km/kWh): '))
			else:
				valor_consumo_combustivel = float(input('Digite o consumo do respectivel combustivel (Km/L): '))
			break

		except:
			print('Resposta inválida, por favor, digite somente números!')	
			linha_vazia()

	coeficiente = coeficientes.get(tipo_combustivel)

	quantidade_carbono = (valor_quilometro / valor_consumo_combustivel) * (coeficiente) 

	return quantidade_carbono

def linha_vazia():
	print('')

if (__name__ ==	 '__main__'):
	calculadora_carbono()
