// Usuário e senha "corretos" para teste (você pode trocar como quiser)
const USUARIO_VALIDO = "admin";
const SENHA_VALIDA = "123456";

const campoNome = document.getElementById("campo-nome");
const campoSenha = document.getElementById("campo-senha");
const botaoLogin = document.getElementById("botao-login");
const mensagemErro = document.getElementById("mensagem-erro");

botaoLogin.addEventListener("click", function (evento) {
    evento.preventDefault(); // impede o link de navegar direto

    const nome = campoNome.value.trim();
    const senha = campoSenha.value.trim();

    if (nome === "" || senha === "") {
        mostrarErro("Preencha usuário e senha.");
        return;
    }

    if (nome === USUARIO_VALIDO && senha === SENHA_VALIDA) {
        // login correto -> redireciona
        window.location.href = "../2inicial/index.html";
    } else {
        mostrarErro("Usuário ou senha incorretos");
    }
});

function mostrarErro(texto) {
    mensagemErro.textContent = texto;
    mensagemErro.style.display = "block";
}