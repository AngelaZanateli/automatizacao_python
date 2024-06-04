    # Passo a passo do projeto

    # 1. Abrir o sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

    # Para instalar: comamand prompt --> pip install pyautogui
import pyautogui as py

py.PAUSE = 0.5
import time

# py.click --> Clicar com o mouse
# py.write --> Escrever um texto
# py.press --> Pressionar uma tecla do teclado
# py.hotkey --> Apretar conjunto de teclas  (Crtl C, Control V, Alt Tab...)
    
# Abrir o navegador (chome) 
py.press("win")
py.write("chrome")
py.press("enter")

# Maximiza o Chrome
py.hotkey('alt', 'space') # Aperta Alt + Espaço
py.press('x') # Seleciona "Maximizar"

#Entrar no site do sistema
py.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
py.press("enter")

# Aqui pode ser que ele demere alguns segundos para carregar o site
time.sleep(2)

# 2. Fazer login
py.click(x=698, y=375)
py.write("angelazanateli@hotmail.com")

py.press("tab") # Passou para o campo de senha
py.write("sua senha aqui")

py.press("tab") # Passou ara o botão de Login
py.press("enter")

time.sleep(1)
# 3. Abri/Importar a base de dados de produtos para cadastrar 
# pip install pandas numpy openpyxl
import pandas as pd

tabela = pd.read_csv("produtos.csv")
# 4. Cadastrar um produto 

for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])

    # Clicar no campo do códgo do produto
    py.click(x=909, y=255)
    py.press("backspace", presses=50)
    # Preencher o código
    py.write(str(codigo))
    # Passar para o próximo canpo
    py.press("tab")  

    # Marca
    py.write(str(tabela.loc[linha, "marca"]))   
    # Passar para o próximo canpo
    py.press("tab")

    # Tipo
    py.write(str(tabela.loc[linha, "tipo"]))
    # Passar para o próximo canpo
    py.press("tab")

    # Categoria
    py.write(str(tabela.loc[linha, "categoria"]))
    # Passar para o próximo canpo
    py.press("tab")

    # Preço
    py.write(str(tabela.loc[linha, "preco_unitario"]))
    # Passar para o próximo canpo
    py.press("tab")

    # Custo
    py.write(str(tabela.loc[linha, "custo"]))
    # Passar para o próximo canpo
    py.press("tab")

    # Obs
    obs = (str(tabela.loc[linha, "obs"]))
    if obs != "nan":
        py.write(obs)
     # Passar para o próximo canpo
    py.press("tab")

    # apertar botão
    py.press("enter")
    py.scroll(5000)

# 5. Repetir isso tudo até acabar a lista de produtos
