 
{
  "testes": [
    {
      "id": 1,
      "nome": "Validacao de campo vazio",
      "descricao": "Deve impedir o envio com o campo de reclamacao vazio",
      "codigo": "describe('Teste 1: Validacao de campo vazio', () => {\n  it('Deve impedir o envio com o campo de reclamacao vazio', () => {\n    cy.visit('index.html');\n    cy.get('.btn-acao').contains('Concluir').click();\n    cy.get('#texto:invalid').should('exist');\n  });\n});"
    },
    {
      "id": 2,
      "nome": "Preenchimento e envio",
      "descricao": "Deve permitir digitar e enviar uma reclamacao",
      "codigo": "describe('Teste 2: Envios de reclamacao', () => {\n  it('Deve permitir digitar e enviar uma reclamacao', () => {\n    cy.visit('index.html');\n    cy.get('#texto').type('O horario do transporte escolar esta atrasado.').should('have.value', 'O horario do transporte escolar esta atrasado.');\n    cy.get('.btn-acao').contains('Concluir').click();\n  });\n});"
    },
    {
      "id": 3,
      "nome": "Exibicao do aviso de ferias",
      "descricao": "Deve exibir a caixa de aviso de ferias escolares na tela",
      "codigo": "describe('Teste 3: Exibicao do aviso de ferias', () => {\n  it('Deve exibir a caixa de aviso de ferias escolares na tela', () => {\n    cy.visit('index.html');\n    cy.get('.caixa-ferias')\n      .should('be.visible')\n      .and('not.be.empty');\n  });\n});"
    }
  ]
}