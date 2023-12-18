import pyautogui 
import time 

pyautogui.alert("Não mexa no computador, o código irá começar a rodar")

pyautogui.pause = 1

pyautogui.press('win')

pyautogui.write('PowerShell')
pyautogui.pause = 1
pyautogui.press('enter')

pyautogui.pause = 1

pyautogui.write('ping https://google.com.br')

pyautogui.pause = 5

pyautogui.write('exit')