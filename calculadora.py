#Para editar a planilha
import pandas as pd

#Para editar a planilha
from openpyxl import load_workbook

#Para arredondar os números
import math

#Funções que a calculadora usa para ler a planilha e fazer as contas
import funcao_calculadora

#Função que contém a calculadora de carbono
def calculadora_carbono():

	#Para escrever a mensagem inicial
	funcao_calculadora.mensagem_inicial()
	
	#Var que recebe a planilha respondida pelo usuário
	planilha = load_workbook(filename = "planilha_medidas.xlsx")

	#Var que recebe a folha da planilha respondida
	sheet_range = planilha['Planilha1']
	#tempo_total = transformar_anos(sheet_range)

	#Divisor para big int
	divisores = 1000000000

	#Valor que cada árvore converte de carbono
	valor_arvore = 0.541

	#Var que recebe a quantidade de carbono produzido em combustão móvel
	carbono_movel = funcao_calculadora.calculo_combustao_movel(sheet_range)

	#Var que receve a quantidade de carbono produzido em combustão aérea
	carbono_aerea = funcao_calculadora.calculo_combustao_aerea(sheet_range)

	#Var que recebe a quantidade de carbono produzido em consumo de energia elétrica 
	carbono_eletrica = funcao_calculadora.energia_eletrica(sheet_range)

	#Var que recebe a quantidade de carbono produzido em consumo de energia estacionária
	carbono_estacionaria = funcao_calculadora.calculo_combustao_estacionaria(sheet_range)

	#Var que recebe o total de carbono produzido pelo usuário
	carbono_final = carbono_movel + carbono_aerea + carbono_eletrica + carbono_estacionaria


	#carbono_final = carbono_final#/ divisores

	#Var que recebe e arrenda para cima a quantidade de árvores que devem ser plantadas
	total_arvores = math.ceil(carbono_final/valor_arvore)

	#Escrever o quanto de carbono o usuário produziu
	print(f'{carbono_final:.3f} tCO2')

	#Escrever quantas árvores ele deve plantar
	print(f'O total de árvores que você deve plantar é {total_arvores}')


#Para chamar a função da calculadora de carbono e garantir que este é o arquivo principal que deve ser lido
if (__name__ == '__main__'):
	calculadora_carbono()
