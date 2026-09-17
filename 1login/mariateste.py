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

    botao_login.click()

    mensagem_erro = driver.find_element(By.ID, "mensagem-erro")

    assert mensagem_erro.is_displayed(), "A mensagem de erro não foi exibida ao enviar campos vazios."
    assert mensagem_erro.text.strip() != "", "A mensagem de erro está vazia."

    print("Teste executado com sucesso: validação de campos vazios OK!")

finally:
    time.sleep(2)
    driver.quit()