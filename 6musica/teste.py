from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializa o navegador
driver = webdriver.Chrome()

# Abre o arquivo HTML local
driver.get(r"C:\Users\aluno\projeto-integrador-3ds-PortalEscolar\6musica\index.html")

# Usa um seletor CSS para achar um elemento estilizado no CSS
elemento = driver.find_element(By.CSS_SELECTOR, ".sua-classe-css")

# Extrai o texto ou valida propriedades do elemento HTML/CSS
print(elemento.text)

driver.quit()
