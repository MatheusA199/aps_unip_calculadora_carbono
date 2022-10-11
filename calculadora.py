import pandas as pd
from openpyxl import load_workbook
import math
import funcao_calculadora


def calculadora_carbono():
	funcao_calculadora.mensagem_inicial()
	
	planilha = load_workbook(filename = "planilha_medidas.xlsx")
	sheet_range = planilha['Planilha1']
	#tempo_total = transformar_anos(sheet_range)
	divisores = 1000000000
	valor_arvore = 0.541
	carbono_movel = funcao_calculadora.calculo_combustao_movel(sheet_range)

	carbono_aerea = funcao_calculadora.calculo_combustao_aerea(sheet_range)

	carbono_eletrica = funcao_calculadora.energia_eletrica(sheet_range)

	carbono_estacionaria = funcao_calculadora.calculo_combustao_estacionaria(sheet_range)

	carbono_final = carbono_movel + carbono_aerea + carbono_eletrica + carbono_estacionaria

	carbono_final = carbono_final#/ divisores
	total_arvores = math.ceil(carbono_final/0.541)
	print(f'{carbono_final:.3f} tCO2')
	print(f'O total de árvores que você deve plantar é {total_arvores}')


if (__name__ == '__main__'):
	calculadora_carbono()
