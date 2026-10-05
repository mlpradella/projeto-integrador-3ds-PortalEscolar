const campoNome = document.getElementById("campo-nome");
const campoSenha = document.getElementById("campo-senha");
const botaoLogin = document.getElementById("botao-login");
const botaoCadastro = document.getElementById("botao-cadastro");
const mensagemErro = document.getElementById("mensagem-erro");

botaoLogin.addEventListener("click", function (evento) {
    evento.preventDefault();
    enviar("/api/login/login", function () {
        window.location.href = "../2inicial/index.html";
    });
});

botaoCadastro.addEventListener("click", function (evento) {
    evento.preventDefault();
    enviar("/api/login/cadastro", function () {
        mostrarMensagem("Cadastro feito! Agora clique em Login.", "#2e7d32");
    });
});

// Envia nome e senha para o servidor.
// "rota" é o endereço (login ou cadastro).
// "aoDarCerto" é o que acontece se o servidor responder ok.
async function enviar(rota, aoDarCerto) {
    const nome = campoNome.value.trim();
    const senha = campoSenha.value;

    if (nome === "" || senha === "") {
        mostrarErro("Preencha usuário e senha.");
        return;
    }

    try {
        const resposta = await fetch(rota, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ nome: nome, senha: senha })
        });
        const dados = await resposta.json();

        if (resposta.ok) {
            aoDarCerto();
        } else {
            mostrarErro(dados.erro);
        }
    } catch (erro) {
        mostrarErro("Não foi possível conectar ao servidor.");
    }
}

function mostrarErro(texto) {
    mostrarMensagem(texto, "#d32f2f");
}

function mostrarMensagem(texto, cor) {
    mensagemErro.textContent = texto;
    mensagemErro.style.color = cor;
    mensagemErro.style.display = "block";
}