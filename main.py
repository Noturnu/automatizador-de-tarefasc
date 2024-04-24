# passo a passo do meu código

# 1: Entrar no sistema da empresa

# 2: fazer login

# 3: Importar os dados 

# 4: cadastrar um produto

# 5; repetira até acabar a bse

import pyautogui
import time
import pandas

pyautogui.PAUSE = 2  


pyautogui.press("win")

pyautogui.write("Opera")

pyautogui.press("enter")

time.sleep(5)

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)

pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=492, y=393)

email = "pedrokleinhans@gmail.com"

pyautogui.write(email)

pyautogui.press("tab")

pyautogui.write("senha123")

pyautogui.click(x=698, y=547)

time.sleep(6)

tabela = pandas.read_csv("produtos.csv")


pyautogui.click(x=868, y=306)

for linha in tabela.index:
    pyautogui.write(tabela.loc [linha, "codigo"])

    pyautogui.press("tab")

    pyautogui.write(tabela.loc [linha, "marca"])

    pyautogui.press("tab")

    pyautogui.write(tabela.loc [linha, "tipo"])

    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc [linha, "categoria"]))

    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc [linha, "preco_unitario"]))

    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc [linha, "custo"]))

    pyautogui.press("tab")

    obs = tabela.loc [linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)

    pyautogui.press("tab")

    pyautogui.press("enter") 

    pyautogui.scroll(5000)   

    pyautogui.click(x=676, y=266)





#pyautogui.click
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

