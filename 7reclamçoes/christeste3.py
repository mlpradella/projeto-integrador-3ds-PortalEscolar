import os
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    caminho_absoluto = os.path.abspath("index.html")
    driver.get(f"file:///{caminho_absoluto}")
    
    caixa_ferias = driver.find_element(By.CLASS_NAME, "caixa-ferias")
    
    assert caixa_ferias.is_displayed(), "A caixa de aviso de férias não está visível na tela"
    assert caixa_ferias.text.strip() != "", "A caixa de aviso de férias está sem conteúdo"

    print("Teste 3 executado com sucesso!")

except Exception as erro:
    print(f"Ocorreu um erro no Teste 3: {erro}")

finally:
    driver.quit()