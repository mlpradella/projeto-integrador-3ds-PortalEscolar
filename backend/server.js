const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
app.use(express.json());

// Mostra as pastas das páginas (1login, 2inicial, 3avisos...)
const raiz = path.join(__dirname, '..');
fs.readdirSync(raiz, { withFileTypes: true })
  .filter(item => item.isDirectory() && /^\d/.test(item.name))
  .forEach(pasta => {
    app.use('/' + pasta.name, express.static(path.join(raiz, pasta.name)));
  });

// Carrega sozinho todo arquivo da pasta "rotas".
// O arquivo avisos.js vira o endereço /api/avisos, e assim por diante.
const pastaRotas = path.join(__dirname, 'rotas');
fs.readdirSync(pastaRotas)
  .filter(arquivo => arquivo.endsWith('.js'))
  .forEach(arquivo => {
    const nome = arquivo.replace('.js', '');
    app.use('/api/' + nome, require(path.join(pastaRotas, arquivo)));
    console.log('Rotas carregadas: /api/' + nome);
  });

app.listen(3000, () => {
  console.log('Servidor rodando em http://localhost:3000');
});