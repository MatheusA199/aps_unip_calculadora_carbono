#Para arrendondar os números
import math

#Pode ser usado para converter a quantidade para anos
def transformar_anos(sheet_range):
	quantidade_anos = int(sheet_range['C3'].value)
	quantidade_tempo_total = quantidade_anos*12 + int(sheet_range['C4'].value)
	return quantidade_tempo_total

#Escrever mensagem inicial do programa
def mensagem_inicial():
	print('************************************************')
	print('*Bem-vindo a calculadora de Crédito de Carbono!*')
	print('************************************************')

#Calcular combustão movel (Carros, ônibus, etc.)
def calculo_combustao_movel(sheet_range):
	#Variavel que recebe a quantidade de carbono produzido
	carbono_final = 0

	#Ideia para trabalhar com big int
	#coeficente_carro = [208000000,237000000,306000000,306000000,92000000,98000000,140000000,350000000,306000000,27000000]

	#Coeficiente de cada carro, multiplicado pelo divisor
	coeficente_carro = [208,237,306,306,92,98,14,35,306,27]

	#Divisores dos coeficientes
	divisores = 1000000

	#Recebe informações da tabela para o calculo, no caso, quilometro
	lista_quilometro = ler_varias_celulas(sheet_range,'D',9,19)	

	#Receber a quantidade de dcarbono produzido
	carbono_final = somar_quantidade_carbono(coeficente_carro,lista_quilometro,carbono_final, divisores)

	#Retorna a quantidade de carbono produzido como resposta
	return carbono_final

#Calcular combustão aerea (Viagens aéreas)
def calculo_combustao_aerea(sheet_range):

	#Coeficiente da viagem de avião
	coeficiente_aviao = [130814]

	#Var que recebe a quantidade de carbono produzido em combustão aérea
	carbono_final = 0

	#Divisor do coeficiente
	divisores = 1000000000

	#Recebe informação da tabela (Quantos quilometros o usuário andou de avião)
	quantidade_quilometro = ler_varias_celulas(sheet_range,'G',9,10)

	#Var que recebe a quantidade de carbono final produzido pelas viagens aéreas
	carbono_final = somar_quantidade_carbono(coeficiente_aviao, quantidade_quilometro,carbono_final,divisores)

	#Retorna como respostaa quantidade de carbono produzido por combustão aérea
	return carbono_final

#Calcular combustão estacionária (Gás encanado e de cozinha)
def calculo_combustao_estacionaria(sheet_range):

	#Var que guarda a quantidade de carbono produzido em combustão aérea
	carbono_final = 0

	#Coefientes de botijão e gás encanado
	coeficente_estacionaria = [40000,2000]

	#coeficente_estacionaria = [40000000,1997000]
	#Divisores do coefiente
	divisores = 1000000

	#Var que recebe as informações do usuário da polanilha
	lista_quantidade = ler_varias_celulas(sheet_range,'I',4,6)	

	#Var que recebe a quantidade de carbono produzido em combustão estacionária
	carbono_final = somar_quantidade_carbono(coeficente_estacionaria, lista_quantidade,carbono_final,divisores)

	#Retorna como resposta a quantidade de carbono produzido por combustão estacionária
	return carbono_final

#Calcular carbono produzido com consumo de energia elétrica
def energia_eletrica(sheet_range):

	#Var que guarda os coefientes de energia elétria(Amapá, Amazônas e Roraima; Demais estados; Internacional)
	coeficiente_energia = [760,51,1500]
	#coeficiente_energia = [760000000,51000000,1500000000]

	#Var que armazena quantidade de carbono produzido 
	carbono_final = 0

	#Divisores de coefientes
	divisores = 1000000

	#Var que recebe as informações da tabela, em relação a quantidade de energia consumida
	lista_gasto = ler_varias_celulas(sheet_range,'H',14,17)

	#Var que recebe a quantidade de carbono produzido
	carbono_final = somar_quantidade_carbono(coeficiente_energia, lista_gasto,carbono_final,divisores)

	#Retorna como repsosta a quantidade de carbono produzido em consumo de energia elétrica
	return carbono_final

#PAra ler as ceculas da planilha respondidas pelo usuário
def ler_varias_celulas(sheet_range,letra,inicio,fim):

	#Var que guarda os valores respondidos
	lista_valores = []

	#Laço que transformará o valor para float e append na lista
	for i in range(inicio,fim):
		try:
			valor = float(sheet_range[f'{letra}{i}'].value)
			
			lista_valores.append(valor)
		except:
			lista_valores.append(0)

	#Retorna os valores respondidos
	return lista_valores

#Para somar/calcular a quantidade de carbono produzido
def somar_quantidade_carbono(coeficiente,lista_valores,carbono_final, divisores):
	#Guarda a quantidade de respostas
	comprimento = len(lista_valores) 

	#Laço que calcula o valor da quantidade de carbono produzido e guarda a resposta na var carbono_final
	for i in range(comprimento):
	
		valores = lista_valores[i] * coeficiente[i] / divisores
		#valores_arredondado = round(valores,2)
		valores_arredondado = math.ceil(valores)
		carbono_final += valores
		
	#Escreve a quantidade de carbono produzido pela emissão em questão
	print(carbono_final)

	#Retorna como respota a quantidade de carbono produzido pela forma de emissão em questão
	return carbono_final
