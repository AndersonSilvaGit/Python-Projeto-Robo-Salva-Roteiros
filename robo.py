""" ROBÔ QUE EXECUTA AS SEQUÊNCIAS DE AÇÕES PARA EXTRAÇÃO DO ROTEIRO."""

import pyautogui
from time import sleep


def open_chrome_in_the_start():
    """ Abre o google chrome, antes de começar a sequência de extração."""
    sleep(1)
    pyautogui.moveTo(706, 744, 0.25)
    pyautogui.click()
    

def save_file(item_number):
    """ Robô que executa todas as ações repetitivas.
        item_number : Número do produto, no qual, o roteiro será extraído"""
    
    WAITFORIT = 1  # Delay padrão para que cada ação seja executada.
    MOUSESPEED = 0.25

    # Abre a janela de pesquisa.
    sleep(WAITFORIT)
    pyautogui.moveTo(802, 230, MOUSESPEED)
    pyautogui.click()
    
    # Digita o número do produto a ser encontrado.
    sleep(WAITFORIT*3)
    pyautogui.write(item_number, interval=0.2)

    # Confirma a escolha.
    for i in range(0, 2):
        sleep(WAITFORIT)
        pyautogui.press('enter')

    # Clica em "imprimir" roteiro.
    sleep(WAITFORIT)
    pyautogui.moveTo(1053, 232, MOUSESPEED)
    pyautogui.click()

    # Clica em Ok.
    sleep(WAITFORIT)
    pyautogui.moveTo(652, 400, MOUSESPEED)
    pyautogui.click()
    sleep(WAITFORIT/2)

    # Escolhe a opção para converter em formato XLS.
    for j in range(0, 3):
        sleep(WAITFORIT/2)
        pyautogui.press('down')

    sleep(WAITFORIT)
    pyautogui.press('enter')

    # Escreve o nome do arquivo.
    sleep(WAITFORIT*1.5)
    new_file_name = item_number
    pyautogui.write(new_file_name, interval=0.2)
    
    # Confirma a escolha e solicita o download do arquivo.
    for k in range(0, 3):
        sleep(WAITFORIT*1.5)
        pyautogui.press('enter')

    # Espera o download do arquivo
    sleep(WAITFORIT*2)

