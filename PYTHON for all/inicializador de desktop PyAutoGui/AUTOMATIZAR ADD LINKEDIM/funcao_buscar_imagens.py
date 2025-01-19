import pyautogui
from time import sleep

def clica_na_imagem(img):
    """
    Função para localizar e clicar em uma imagem na tela.
    Retorna True se encontrou e clicou, False caso contrário.
    """
    try:
        # Corrigindo o caminho para apontar para a pasta correta
        imagem = f"C:/PYTHON for All/inicializador de desktop PyAutoGui/AUTOMATIZAR ADD LINKEDIM/img/{img}.png"
        sleep(1)
        
        # Tentativa de localizar a imagem
        local_imagem = pyautogui.locateOnScreen(imagem, confidence=0.9)
        
        if local_imagem is not None:
            pyautogui.click(local_imagem)
            return True
        else:
            print(f"Imagem {img} não encontrada na tela")
            return False
    except Exception as e:
        print(f"Erro ao procurar/clicar na imagem: {e}")
        return False