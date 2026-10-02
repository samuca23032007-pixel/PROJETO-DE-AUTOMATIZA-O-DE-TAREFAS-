#bibliotecas = pacotes de código
# pip install pyautogui -> instala a biblioteca pyautogui

import pyautogui 
import time # permite fazer o controle de tempo do programa
#pyautogui.click -> clica
#pyautogui.write -> escreve um texto 
#pyaitogui.press -> aperta uma tecla 
#pyautogui.hotkey -> aperta um atalho (hotKey)

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Resumo: todos esses comandos são usados para automatizar tarefas no computador, como clicar em botões,
# escrever textos, apertar teclas e usar atalhos de teclado.

#Passo a passo do seu programa
#Passo 1: Entrar no sistema da empresa
#abriria o navegador 
pyautogui.press ("win") # -> vai apertar a tecla windows
pyautogui.write ("chrome") # -> vai escrever "chrome" na barra de pesquisa
pyautogui.press ("enter") # -> vai apertar a tecela enter 

time.sleep(5)

pyautogui.write (link) # -> vai escrever o link do sistema da empresa
pyautogui.press ("enter") 
#fazer uma pausa maior pro site carregar 
time.sleep(5)


#Passo 2: Fazer login no sistema da empresa
#clicar no campo de email
pyautogui.click(x= 556, y= 411) # vai cliclar no campo de email
pyautogui.write ("pythonimpressionador@gmail.com") # vai escrever o email no campo de email
time.sleep(3)
pyautogui.press("tab") # passar para o campo de senha

pyautogui.write("senha123") # vai escrever a senha no campo de senha 
pyautogui.press("tab")
pyautogui.press("enter") # vai apertar o botão de login
pyautogui.press("enter") #vai apertar o botão pela segunda vez 
#fazer uma pausa maior pro site carregar 



# Passo 3: abrir a base de dados da empresa
import pandas 

tabela = pandas.read_csv("produtos (1).csv") # vai abrir a base de dados da empresa e armazenar na variável tabela
print(tabela)


for linha in tabela.index: # vai percorrer todas as linhas da base de dados 
    #Passo 4: Cadastrar 1 produto no sistema da empresa
    pyautogui.click(x = 567, y=291) 
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab") # passar para o próximo campo


    # marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    #preço
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab") # Passar para o botao enviar 

    pyautogui.press("enter") #pressiona o botão enviar para cadastra o produto no sistema da empresa
    # voltar para o inicio da tela 

    pyautogui.scroll(5000) # o número dentro de parenteses é a quantidade de pixels que ele vai subir ou descer na tela, se for positivo ele sobe, se for negativo ele desce

# Passo 5: Cadastrar todos os produtos da base de dados no sistema da empresa


