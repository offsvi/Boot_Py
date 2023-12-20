import pyautogui 
import time 

pyautogui.alert("Não mexa no computador, o código irá começar a rodar")

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