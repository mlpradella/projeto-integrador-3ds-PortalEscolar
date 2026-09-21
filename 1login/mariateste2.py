import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://127.0.0.1:5500/1login/index.html")
    driver.maximize_window()

    campo_nome = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Name']")
    campo_senha = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
    botao_login = driver.find_element(By.CSS_SELECTOR, ".botao")

    campo_nome.send_keys("admin")
    campo_senha.send_keys("123456")

    botao_login.click()

    time.sleep(1)  # espera a navegação/redirecionamento acontecer

    assert "2inicial" in driver.current_url, "Não redirecionou para a página inicial após login correto."

    print("Teste executado com sucesso: login com credenciais corretas validado!")

finally:
    time.sleep(2)
    driver.quit()