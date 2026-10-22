from flask import Flask, request, jsonify # type: ignore
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)

banco_de_dados = {
    "mes": "Julho",
    "dias_no_mes": 31,
    "eventos": {}
}

@app.route('/api/calendario', methods=['GET'])
def obter_calendario():
    return jsonify(banco_de_dados), 200

@app.route('/api/calendario/evento', methods=['POST'])
def salvar_evento():
    dados = request.get_json()
    dia = int(dados.get('dia'))
    titulo = dados.get('titulo')

    if dia not in banco_de_dados['eventos']:
        banco_de_dados['eventos'][dia] = []

    banco_de_dados['eventos'][dia].append(titulo)
    return jsonify({"mensagem": "Evento adicionado!"}), 200

# Nova Rota para DELETAR eventos
@app.route('/api/calendario/evento', methods=['DELETE'])
def deletar_evento():
    dados = request.get_json()
    dia = int(dados.get('dia'))
    index = dados.get('index')

    if dia in banco_de_dados['eventos'] and 0 <= index < len(banco_de_dados['eventos'][dia]):
        banco_de_dados['eventos'][dia].pop(index)
        return jsonify({"mensagem": "Evento removido!"}), 200

    return jsonify({"erro": "Evento não encontrado"}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)