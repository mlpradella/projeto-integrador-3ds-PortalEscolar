from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    # Abre o arquivo index.html diretamente na pasta 9aviso2
    driver.get(r"file:///C:/Users/aluno/projeto-integrador-3ds-PortalEscolar/9aviso2/index.html")

    # 1. Localiza o card principal de avisos
    card_jogos = driver.find_element(By.ID, "card-jogos")

    # TESTE 1: Verificar se o card de avisos está visível
    assert card_jogos.is_displayed(), "O card de avisos dos Jogos Escolares não está visível!"
    print("Sucesso: O card dos Jogos Escolares está visível na tela.")

    # TESTE 2: Validar informações de local e horário
    info_sala = driver.find_element(By.ID, "info-sala").text
    info_horario = driver.find_element(By.ID, "info-horario").text

    assert "Quadra" in info_sala, "O local do jogo esperado não é 'Quadra'!"
    assert "09:00" in info_horario, "O horário esperado não é '09:00'!"
    print(f"Sucesso: Local ('{info_sala}') e Horário ('{info_horario}') validados!")

    # TESTE 3: Validar responsáveis
    responsaveis = driver.find_element(By.ID, "info-responsaveis").text
    assert "Debora e Ademar" in responsaveis, "Os nomes dos responsáveis não correspondem!"
    print("Sucesso: Nomes dos responsáveis validados com sucesso!")

finally:
    driver.quit()