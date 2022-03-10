import time
import pyautogui ##importa rotinas prontas  


##Aperta alt para baixo
pyautogui.keyDown('alt') 
##pressiona o TAB
pyautogui.press('tab') 
##Solta a tecla alt
pyautogui.keyUp('alt') 
##Digita o texto desejado 

print('Clicando em Troubleshoot')
time.sleep(2) ##Aguardando 2 segundos
pyautogui.click(1178,364) ##botão troboshuts
time.sleep(5) ##Aguardando 5 segundos

print('Clicando em Manually accept notification')
time.sleep(2) ##Aguardando 2 segundos
pyautogui.click(470,713)

print('Clicando ok')
time.sleep(2) ##Aguardando 2 segundos
pyautogui.click(1000,179)


