import os
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    # Obtém o caminho absoluto exato do arquivo HTML no seu Windows
    caminho_absoluto = os.path.abspath("index.html")
    driver.get(f"file:///{caminho_absoluto}")
    
    # Clica no botão
    botao = driver.find_element(By.CLASS_NAME, "btn-acao")
    if "Concluir" in botao.text:
        botao.click()
    
    # Valida se o campo está inválido (vazio)
    campo_texto = driver.find_element(By.ID, "texto")
    is_invalid = driver.execute_script("return !arguments[0].checkValidity();", campo_texto)
    
    assert is_invalid, "O campo de reclamação deveria estar inválido por estar vazio"
    print("Teste 1 executado com sucesso!")

finally:
    driver.quit()