import os
# Obtém o diretório do arquivo atual
caminho_atual = os.path.dirname(os.path.abspath(__file__))
# Define o diretório de trabalho como o diretório do arquivo
os.chdir(caminho_atual)
print(caminho_atual)
print(str(caminho_atual))
print('aqui')
print(type(caminho_atual))