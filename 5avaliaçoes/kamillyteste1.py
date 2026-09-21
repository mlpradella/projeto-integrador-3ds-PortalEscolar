import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Endereço da página de avaliações (aberta direto do computador, sem Live Server)
# O ç da pasta vai codificado como %C3%A7
URL = "file:///C:/Users/aluno/projeto-integrador-3ds-PortalEscolar/5avalia%C3%A7oes/index.html"


# ---------- TESTE 1: ACERTO ----------
# Confere se o que deveria aparecer na página realmente aparece.
def teste_acerto():
    driver = webdriver.Chrome()

    try:
        driver.get(URL)
        driver.maximize_window()

        titulo = driver.find_element(By.TAG_NAME, "h1")
        cards = driver.find_elements(By.CLASS_NAME, "caixas")

        assert titulo.text == "AVALIAÇÕES", "O título da página está diferente do esperado."
        assert len(cards) == 3, f"Eram esperados 3 cards, mas foram encontrados {len(cards)}."

        assert "Matemática" in cards[0].text and "08:00" in cards[0].text, "Card de Matemática incorreto."
        assert "Português" in cards[1].text and "09:30" in cards[1].text, "Card de Português incorreto."
        assert "Geografia" in cards[2].text and "11:30" in cards[2].text, "Card de Geografia incorreto."

        print("Teste de acerto executado com sucesso: título e cards validados!")

    finally:
        time.sleep(2)
        driver.quit()


print("Iniciando o teste...")

teste_acerto()

print("Teste terminou.")