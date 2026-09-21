import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Endereço da página de avaliações (aberta direto do computador, sem Live Server)
# O ç da pasta vai codificado como %C3%A7
URL = "file:///C:/Users/aluno/projeto-integrador-3ds-PortalEscolar/5avalia%C3%A7oes/index.html"


# ---------- TESTE 2: ERRO ----------
# Confere se o que NÃO deveria existir realmente não existe.
def teste_erro():
    driver = webdriver.Chrome()

    try:
        driver.get(URL)
        driver.maximize_window()

        # find_elements devolve uma lista vazia quando não encontra nada
        avaliacao_falsa = driver.find_elements(By.ID, "avaliacao-de-quimica")
        texto_da_pagina = driver.find_element(By.TAG_NAME, "body").text

        assert len(avaliacao_falsa) == 0, "Foi encontrado um elemento que não deveria existir."
        assert "Química" not in texto_da_pagina, "Uma matéria não cadastrada apareceu na página."

        print("Teste de erro executado com sucesso: nada indevido apareceu na página!")

    finally:
        time.sleep(2)
        driver.quit()


print("Iniciando o teste...")

teste_erro()

print("Teste terminou.")