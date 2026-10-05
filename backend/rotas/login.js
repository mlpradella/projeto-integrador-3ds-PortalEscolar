const express = require('express');
const bcrypt = require('bcryptjs');
const db = require('../banco');

const router = express.Router();

// Cria a tabela de alunos, se ainda não existir
db.exec(`
  CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
  )
`);

// CADASTRO: POST /api/login/cadastro
router.post('/cadastro', async (req, res) => {
  const { nome, senha } = req.body;
  if (!nome || !senha) {
    return res.status(400).json({ erro: 'Preencha usuário e senha.' });
  }

  const existe = db.prepare('SELECT id FROM alunos WHERE nome = ?').get(nome);
  if (existe) {
    return res.status(409).json({ erro: 'Esse aluno já está cadastrado.' });
  }

  const hash = await bcrypt.hash(senha, 10);
  db.prepare('INSERT INTO alunos (nome, senha) VALUES (?, ?)').run(nome, hash);
  res.status(201).json({ ok: true });
});

// LOGIN: POST /api/login/login
router.post('/login', async (req, res) => {
  const { nome, senha } = req.body;
  if (!nome || !senha) {
    return res.status(400).json({ erro: 'Preencha usuário e senha.' });
  }

  const aluno = db.prepare('SELECT * FROM alunos WHERE nome = ?').get(nome);
  const senhaCorreta = aluno && await bcrypt.compare(senha, aluno.senha);

  if (!senhaCorreta) {
    return res.status(401).json({ erro: 'Usuário ou senha incorretos' });
  }
  res.json({ ok: true });
});

module.exports = router;