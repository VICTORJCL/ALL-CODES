import os
import pyautogui
import os
from time import sleep
from dotenv import load_dotenv
import webbrowser
# tempo
import time
from datetime import datetime, timedelta

from funcao_buscar_imagens import clica_na_imagem
os.chdir('C:/PYTHON for All/inicializador de desktop PyAutoGui/AUTOMATIZAR ADD LINKEDIM/img')

load_dotenv()

# curitiba e região, tech recruiter
webbrowser.open('https://www.linkedin.com/search/results/people/?geoUrn=%5B%2290009579%22%5D&keywords=tech%20recruiter&origin=FACETED_SEARCH&sid=C2e')
# pyautogui.write("tech recruiter", interval=0.10)



def loop_por_tempo():
    # Define o tempo de término (10 minutos a partir de agora)
    tempo_final = datetime.now() + timedelta(minutes=10)
    
    try:
        while datetime.now() < tempo_final:
            # Seu código aqui
            sleep(3)
            clica_na_imagem('pessoas')
            sleep(2)
            clica_na_imagem('conectar')
            sleep(1)
            clica_na_imagem('enviar')
            sleep(1)
            clica_na_imagem('entendi')
            pyautogui.press("pagedown")
            sleep(1)
            
            # Opcional: adicione um pequeno delay para não sobrecarregar o CPU
            time.sleep(1)  # Espera 1 segundo entre execuções
        
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário")

sleep(3)
clica_na_imagem('pessoas')
sleep(2)

pyautogui.press("pagedown")
sleep(1)
clica_na_imagem('conectar')
sleep(1)
clica_na_imagem('enviar')







# webbrowser.open('https://www.linkedin.com/in/victor-jos%C3%A9-costta-lameiro-09b3a8258/')
''' beta_1
sleep(3)
clica_na_imagem('Pesquisa')
pyautogui.write("tech recruiter", interval=0.10)
pyautogui.press("enter")
sleep(3)
clica_na_imagem('pessoas')
sleep(2)

pyautogui.press("pagedown")
sleep(1)
clica_na_imagem('conectar')
sleep(1)
clica_na_imagem('enviar')
'''


'''
sleep(1)
pyautogui.hotkey("ctrl", "shift", "n")
sleep(1)
pyautogui.hotkey("ctrl", "l")
sleep(1)
pyautogui.write("RSCL3 ", interval=0.10)
pyautogui.press("enter")
sleep(1)
pyautogui.press("pagedown")
pyautogui.press("pagedown")


clica_na_imagem('Icon_Tradingview')
sleep(1)
pyautogui.press("enter")

 lista de coisas pyautogui
pyautogui.hotkey("ctrl", "shift", "n")
pyautogui.write("google", interval=0.10)
pyautogui.press("space")
pyautogui.write("globo.com", interval=0.10)
pyautogui.write(SENHA_GOOGLE, interval=0.10)
sleep(1)
'''