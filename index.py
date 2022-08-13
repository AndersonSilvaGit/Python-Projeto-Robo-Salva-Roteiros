""" PROGRAMA CRIADO PARA EXTRAIR OS ROTEIROS DE 
    FABRICAÇÃO DO ANTIGO ERP DA EMPRESA.

    CRIADO POR: ANDERSON SILVA 06/07/2022. """

import openpyxl
from pathlib import Path
import robo

# Carrega as informações contidas no arquivo de Excel.
file_name = 'itens.xlsx'
excel_file = openpyxl.open(Path('dataset', file_name))
excel_sheet = excel_file['produtos']

# Armazena as informação em uma lista.
item_list = list()
for rowNumber in range(1, excel_sheet.max_row+1):
    item_list.append(excel_sheet.cell(row=rowNumber, column=1).value)

# Abre o google chrome para iniciar a sequência de repetições
robo.open_chrome_in_the_start()

# Executa o robô para cada número de item na lista.
for itemNumber in item_list:
    robo.save_file(itemNumber)

