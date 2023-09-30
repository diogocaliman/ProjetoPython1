# Passo a passo do projeto 

# 1 : Entrar no Sistema

import pyautogui # para install: pip install pyautogui
import time
# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> atalho

pyautogui.PAUSE = 0.5

# abrir o chrome

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


# entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# esperar o site carregar
time.sleep(3)

# -----------------------------------------------------------------------------

# 2 : Fazer login

pyautogui.click(x=2607, y=397)
pyautogui.write("diogocaliman@outlook.com")

pyautogui.press("tab")
pyautogui.write("Senha123")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)


# 3 : Importar os dados do produto
# pip install pandas numpy openpyxl

import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)


for linha in tabela.index:

    # 4 : Cadastro

    pyautogui.click(x=2625, y=279)

    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    

    # preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

        
    # enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
   
# 5 : Repetir o cadastro



    