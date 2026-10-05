const express = require('express');
const db = require('../banco');

const router = express.Router();

// Senha do professor. TROQUE por uma senha sua!
const SENHA_ADMIN = process.env.SENHA_ADMIN || 'professor123';

db.exec(`
  CREATE TABLE IF NOT EXISTS avisos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    data TEXT NOT NULL,
    descricao TEXT,
    detalhes TEXT
  )
`);

// LIMPEZA TEMPORÁRIA: apaga os 3 avisos antigos que foram para o banco por engano.
// Rode o servidor uma vez com isto e depois APAGUE este bloco.
db.prepare(`
  DELETE FROM avisos
  WHERE (titulo = 'Reunião de pais' AND data = '08/08/2026')
     OR (titulo = 'Jogos escolares' AND data = '08/09/2026 e 15/09/2026')
     OR (titulo = 'Férias' AND data = '06/06/2026 a 26/07/2026')
`).run();

// Porteiro: só deixa passar quem mandar a senha certa
function somenteAdmin(req, res, next) {
  if (req.get('x-admin-senha') !== SENHA_ADMIN) {
    return res.status(401).json({ erro: 'Senha de administrador incorreta.' });
  }
  next();
}

// LISTAR: GET /api/avisos
router.get('/', (req, res) => {
  const avisos = db.prepare('SELECT * FROM avisos ORDER BY id').all();
  res.json(avisos);
});

// BUSCAR um aviso: GET /api/avisos/1
router.get('/:id', (req, res) => {
  const aviso = db.prepare('SELECT * FROM avisos WHERE id = ?').get(req.params.id);
  if (!aviso) {
    return res.status(404).json({ erro: 'Aviso não encontrado.' });
  }
  res.json(aviso);
});

// CRIAR (só professor): POST /api/avisos
router.post('/', somenteAdmin, (req, res) => {
  const { titulo, data, descricao, detalhes } = req.body;
  if (!titulo || !data) {
    return res.status(400).json({ erro: 'Título e data são obrigatórios.' });
  }
  db.prepare(
    'INSERT INTO avisos (titulo, data, descricao, detalhes) VALUES (?, ?, ?, ?)'
  ).run(titulo, data, descricao || '', detalhes || '');
  res.status(201).json({ ok: true });
});

// APAGAR (só professor): DELETE /api/avisos/1
router.delete('/:id', somenteAdmin, (req, res) => {
  db.prepare('DELETE FROM avisos WHERE id = ?').run(req.params.id);
  res.json({ ok: true });
});

module.exports = router;