from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# Abrindo a tela de LOGIN para testar os inputs reais
driver.get(r"C:\Users\aluno\projeto-integrador-3ds-PortalEscolar\1login\index.html")

try:
    # 1. Localiza o campo de usuário/email (geralmente a tag input)
    # Se der erro, mude para By.ID caso seu HTML tenha 'id="usuario"' ou 'id="email"'
    campo_usuario = driver.find_element(By.TAG_NAME, "input")
    
    # 2. Digita um usuário de teste
    campo_usuario.send_keys("aluno@escola.com")
    
    print("Teste 2 (Input de Login): Passou com sucesso!")

except Exception as e:
    print(f"Teste 2 Falhou: {e}")

finally:
    driver.quit()
