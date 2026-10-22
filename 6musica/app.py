from flask import Flask, request, jsonify
from flask_cors import CORS
import json, os

app = Flask(__name__)
CORS(app)

ARQUIVO = 'recomendacoes.json'

def carregar():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar(lista):
    with open(ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False, indent=2)

@app.route('/recomendar', methods=['POST'])
def recomendar():
    dados = request.get_json()
    lista = carregar()
    lista.append({
        'musica': dados.get('musica'),
        'artista': dados.get('artista'),
        'minutagem': dados.get('minutagem')
    })
    salvar(lista)
    return jsonify({'mensagem': f'Recomendação de "{dados.get("musica")}" salva com sucesso!'}), 201

@app.route('/recomendacoes', methods=['GET'])
def listar():
    return jsonify(carregar())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8082, debug=True)