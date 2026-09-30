import os
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    caminho_absoluto = os.path.abspath("index.html")
    driver.get(f"file:///{caminho_absoluto}")
    
    campo_texto = driver.find_element(By.ID, "texto")
    mensagem = "O horário do transporte escolar está atrasado."
    campo_texto.send_keys(mensagem)
    
    assert campo_texto.get_attribute("value") == mensagem, "O texto digitado não confere"
    
    botao = driver.find_element(By.CLASS_NAME, "btn-acao")
    if "Concluir" in botao.text:
        botao.click()

    print("Teste 2 executado com sucesso!")

finally:
    driver.quit()