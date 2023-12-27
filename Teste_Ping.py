#Importando biblioteca Pyautogui e Time 
import pyautogui 
import time 

# Alert irá mostrar uma janela com o texto das aspas 
pyautogui.alert("Não mexa no computador, o código irá começar a rodar")

# Pause utiliza a biblioteca time e utiliza uma pausa entre um código e outro
pyautogui.PAUSE = 2


pyautogui.press("win")

pyautogui.write("PowerShell")
pyautogui.PAUSE = 2
pyautogui.press("enter")

pyautogui.PAUSE = 2

pyautogui.write("ping 192.168.75.1")
pyautogui.press("enter") 

pyautogui.PAUSE = 6 

pyautogui.write("gpupdate /force")
pyautogui.press("enter")
pyautogui.PAUSE = 12

pyautogui.write("exit")
pyautogui.press("enter")