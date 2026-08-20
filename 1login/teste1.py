import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializa o navegador
driver = webdriver.Chrome()

try:
    # 1. Abre a sua página de login
    driver.get("http://127.0.0.1:5500/1login/index.html")  # Substitua pelo seu endereço local
    driver.maximize_window()

    # 2. Mapeia os elementos usando os seletores do seu HTML/CSS
    campo_nome = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Name']")
    campo_senha = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
    botao_login = driver.find_element(By.CSS_SELECTOR, ".botao")

    # 3. Preenche credenciais inválidas
    campo_nome.send_keys("usuario_falso")
    campo_senha.send_keys("123456")

    # 4. Executa a ação de clique
    botao_login.click()

    # 5. Validação (Exemplo com validação de mensagem de erro)
    # Obs: Requer o elemento de erro implementado no HTML
    mensagem_erro = driver.find_element(By.ID, "mensagem-erro")
    
    # Garante que a mensagem está visível e contém o texto esperado
    assert mensagem_erro.is_displayed(), "A mensagem de erro não foi exibida na tela."
    assert "Usuário ou senha incorretos" in mensagem_erro.text, "Texto da mensagem divergente."

    print("Teste executado com sucesso: mensagem de erro validada!")

finally:
    time.sleep(2)
    driver.quit()