from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    # 1. Abre a página do calendário usando o caminho do seu computador
    driver.get(r"file:///C:/Users/aluno/projeto-integrador-3ds-PortalEscolar/4calendario/index.html")

    # 2. Localiza o botão "Voltar" pela classe CSS
    botao_voltar = driver.find_element(By.CLASS_NAME, "btn-voltar")

    # TESTE A: Verificar se o botão está visível na tela
    assert botao_voltar.is_displayed(), "O botão Voltar não está visível!"
    print("Sucesso: O botão 'Voltar' está visível na página.")

    # TESTE B: Clicar no botão e verificar a navegação
    botao_voltar.click()

    # Obtém o novo endereço (URL) em que o navegador se encontra
    url_atual = driver.current_url
    print(f"URL após o clique: {url_atual}")

    # Confirma se o navegador tentou ir para a página inicial (index.html da pasta 2inicial)
    assert "2inicial" in url_atual, "O botão não redirecionou para a pasta 2inicial!"
    print("Sucesso: Navegação do botão 'Voltar' funcionou corretamente!")

finally:
    driver.quit()