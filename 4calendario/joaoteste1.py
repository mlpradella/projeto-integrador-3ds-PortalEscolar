from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    # Aponta diretamente para o arquivo HTML da sua pasta
    driver.get(r"file:///C:/Users/aluno/projeto-integrador-3ds-PortalEscolar/4calendario/index.html")

    # Agora o Selenium encontrará o elemento
    titulo_mes = driver.find_element(By.ID, "titulo-mes")
    
    print(f"Texto encontrado: '{titulo_mes.text}'")
    assert "julho" in titulo_mes.text.lower(), "O título não contém a palavra Julho!"
    print("Teste passou com sucesso!")

finally:
    driver.quit()