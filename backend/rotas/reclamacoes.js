const express = require('express');
const cors = require('cors');
const mysql = require('mysql2');

const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

// Conexão com o banco MySQL
const db = mysql.createConnection({
  host: '127.0.0.1',
  user: 'root',
  password: '',
  database: 'E-commerce'
});

db.connect((err) => {
  if (err) {
    console.error('Erro ao conectar ao banco MySQL:', err.message);
  } else {
    console.log('Conectado ao banco de dados MySQL com sucesso!');
  }
});

// Rota GET: Buscar reclamações
app.get('/api/reclamacoes', (req, res) => {
  const query = 'SELECT * FROM reclamacoes ORDER BY data_envio DESC';

  db.query(query, (err, resultados) => {
    if (err) {
      console.error('Erro ao consultar banco:', err);
      return res.status(500).json({ erro: 'Erro ao buscar dados do banco.' });
    }
    return res.status(200).json(resultados);
  });
});

// Rota POST: Salvar nova reclamação
app.post('/api/reclamacoes', (req, res) => {
  const { mensagem } = req.body; // A variável 'mensagem' é criada AQUI dentro

  if (!mensagem || mensagem.trim() === '') {
    return res.status(400).json({ erro: 'A mensagem não pode estar vazia.' });
  }

  const query = 'INSERT INTO reclamacoes (texto, data_envio) VALUES (?, NOW())';

  db.query(query, [mensagem], (err, result) => {
    if (err) {
      console.error('Erro ao salvar no banco:', err);
      return res.status(500).json({ erro: 'Erro ao armazenar mensagem.' });
    }

    console.log(`Reclamação gravada com sucesso! ID: ${result.insertId}`);
    return res.status(201).json({ mensagem: 'mensagem armazenada' });
  });
});

app.listen(PORT, () => {
  console.log(`Servidor rodando em: http://localhost:${PORT}`);
});