import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Endereço da página de avaliações (aberta direto do computador, sem Live Server)
# O ç da pasta vai codificado como %C3%A7
URL = "file:///C:/Users/aluno/projeto-integrador-3ds-PortalEscolar/5avalia%C3%A7oes/index.html"


# ---------- TESTE 3: INTERAÇÃO ----------
# Simula o usuário clicando no botão Voltar.
def teste_interacao():
    driver = webdriver.Chrome()

    try:
        driver.get(URL)
        driver.maximize_window()

        botao_voltar = driver.find_element(By.LINK_TEXT, "Voltar")

        botao_voltar.click()
        time.sleep(1)

        assert "2inicial" in driver.current_url, "O botão Voltar não levou para a página inicial."

        print("Teste de interação executado com sucesso: o botão Voltar levou para a página inicial!")

    finally:
        time.sleep(2)
        driver.quit()


print("Iniciando o teste...")

teste_interacao()

print("Teste terminou.")