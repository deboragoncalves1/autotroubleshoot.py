import time
import pyautogui ##importa rotinas prontas  

cont=0
while cont<100:
    cont= cont+1
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
    
    print('Atualizando a página')
    time.sleep(5) ##Aguardando 2 segundos
    pyautogui.click(117,46)
    
    print(cont)
