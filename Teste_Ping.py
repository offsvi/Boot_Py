import pyautogui 
import time 

pyautogui.alert("Não mexa no computador, o código irá começar a rodar")

pyautogui.pause = 1

pyautogui.press('win')

pyautogui.write('PowerShell')
pyautogui.press('enter')