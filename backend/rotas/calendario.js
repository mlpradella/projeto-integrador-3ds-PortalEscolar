const express = require('express');
const fs = require('fs');
const path = require('path');

const router = express.Router();
const ARQUIVO = path.join(__dirname, 'eventos.json');
const TIPOS_VALIDOS = ['avaliacao', 'trabalho', 'outro'];

function lerEventos() {
    if (!fs.existsSync(ARQUIVO)) return [];
    try {
        return JSON.parse(fs.readFileSync(ARQUIVO, 'utf-8'));
    } catch (erro) {
        console.error('eventos.json inválido, começando vazio.', erro);
        return [];
    }
}

function salvarEventos(eventos) {
    fs.writeFileSync(ARQUIVO, JSON.stringify(eventos, null, 2), 'utf-8');
}

function dataValida(data) {
    return typeof data === 'string' && /^\d{4}-\d{2}-\d{2}$/.test(data);
}

// Listar eventos
router.get('/', (req, res) => {
    let eventos = lerEventos();
    if (req.query.data) {
        eventos = eventos.filter(e => e.data === req.query.data);
    }
    res.json(eventos);
});

// Criar evento
router.post('/', (req, res) => {
    const { titulo, tipo, data, descricao } = req.body || {};

    if (!titulo || typeof titulo !== 'string' || !titulo.trim()) {
        return res.status(400).json({ erro: 'O título é obrigatório.' });
    }
    if (!dataValida(data)) {
        return res.status(400).json({ erro: 'A data deve estar no formato AAAA-MM-DD.' });
    }

    const novo = {
        id: Date.now(),
        titulo: titulo.trim().slice(0, 80),
        tipo: TIPOS_VALIDOS.includes(tipo) ? tipo : 'outro',
        data,
        descricao: typeof descricao === 'string' ? descricao.trim().slice(0, 300) : ''
    };

    const eventos = lerEventos();
    eventos.push(novo);
    salvarEventos(eventos);

    res.status(201).json(novo);
});

// Apagar evento
router.delete('/:id', (req, res) => {
    const id = Number(req.params.id);
    const eventos = lerEventos();
    const restantes = eventos.filter(e => e.id !== id);

    if (restantes.length === eventos.length) {
        return res.status(404).json({ erro: 'Evento não encontrado.' });
    }

    salvarEventos(restantes);
    res.status(204).end();
});

module.exports = router;