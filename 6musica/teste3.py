from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get(r"C:\Users\aluno\projeto-integrador-3ds-PortalEscolar\6musica\index.html")

try:
    # 1. Clica no botão/link Voltar da sua página de música
    botao_navegacao = driver.find_element(By.LINK_TEXT, "Voltar")
    botao_navegacao.click()
    
    # 2. Pega a URL de destino
    url_atual = driver.current_url
    
    # 3. VALIDAÇÃO: Verifica se fomos para a pasta da página inicial
    assert "2inicial" in url_atual, "O link não navegou para a página inicial esperada!"
    print(f"Teste 3 (Navegação): Passou com sucesso! Foi para: {url_atual}")

except Exception as e:
    print(f"Teste 3 Falhou: {e}")

finally:
    driver.quit()
