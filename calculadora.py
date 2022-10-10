import pandas as pd
from openpyxl import load_workbook
import math


def calculadora_carbono():
	mensagem_inicial()

	
	planilha = load_workbook(filename = "planilha_medidas.xlsx")
	sheet_range = planilha['Planilha1']
	#tempo_total = transformar_anos(sheet_range)
	divisores = 1000000000
	valor_arvore = 0.541
	carbono_movel = calculo_combustao_movel(sheet_range)

	carbono_aerea = calculo_combustao_aerea(sheet_range)

	carbono_eletrica = energia_eletrica(sheet_range)

	carbono_estacionaria = calculo_combustao_estacionaria(sheet_range)

	carbono_final = carbono_movel + carbono_aerea + carbono_eletrica + carbono_estacionaria

	carbono_final = carbono_final#/ divisores
	total_arvores = math.ceil(carbono_final/0.541)
	print(f'{carbono_final:.3f} tCO2')
	print(f'O total de árvores que você deve plantar é {total_arvores}')

def transformar_anos(sheet_range):
	quantidade_anos = int(sheet_range['C3'].value)
	quantidade_tempo_total = quantidade_anos*12 + int(sheet_range['C4'].value)
	return quantidade_tempo_total


def mensagem_inicial():
	print('************************************************')
	print('*Bem-vindo a calculadora de Crédito de Carbono!*')
	print('************************************************')

def calculo_combustao_movel(sheet_range):
	sheet_range = sheet_range
	carbono_final = 0
	#coeficente_carro = [208000000,237000000,306000000,306000000,92000000,98000000,140000000,350000000,306000000,27000000]
	coeficente_carro = [208,237,306,306,92,98,14,35,306,27]

	divisores = 1000000
	lista_quilometro = ler_varias_celulas(sheet_range,'D',9,19)	

	carbono_final = somar_quantidade_carbono(coeficente_carro,lista_quilometro,carbono_final, divisores)
	return carbono_final


def calculo_combustao_aerea(sheet_range):
	coeficiente_aviao = [130814]
	carbono_final = 0
	divisores = 1000000000
	quantidade_quilometro = ler_varias_celulas(sheet_range,'G',9,10)
	carbono_final = somar_quantidade_carbono(coeficiente_aviao, quantidade_quilometro,carbono_final,divisores)

	return carbono_final

def calculo_combustao_estacionaria(sheet_range):
	sheet_range = sheet_range
	carbono_final = 0
	coeficente_estacionaria = [40000,2000]
	#coeficente_estacionaria = [40000000,1997000]
	divisores = 1000000
	lista_quantidade = ler_varias_celulas(sheet_range,'I',4,6)	
	carbono_final = somar_quantidade_carbono(coeficente_estacionaria, lista_quantidade,carbono_final,divisores)

	return carbono_final

def energia_eletrica(sheet_range):
	coeficiente_energia = [760,51,1500]
	#coeficiente_energia = [760000000,51000000,1500000000]

	carbono_final = 0
	divisores = 1000000
	lista_gasto = ler_varias_celulas(sheet_range,'H',14,17)
	carbono_final = somar_quantidade_carbono(coeficiente_energia, lista_gasto,carbono_final,divisores)

	return carbono_final


def ler_varias_celulas(sheet_range,letra,inicio,fim):
	lista_valores = []
	for i in range(inicio,fim):
		try:
			valor = float(sheet_range[f'{letra}{i}'].value)
			
			lista_valores.append(valor)
		except:
			lista_valores.append(0)

	return lista_valores

def somar_quantidade_carbono(coeficiente,lista_valores,carbono_final, divisores):

	comprimento = len(lista_valores) 

	for i in range(comprimento):
	
		valores = lista_valores[i] * coeficiente[i] / divisores
		#valores_arredondado = round(valores,2)
		valores_arredondado = math.ceil(valores)
		carbono_final += valores
		
	print(carbono_final)
	return carbono_final




if (__name__ == '__main__'):
	calculadora_carbono()
