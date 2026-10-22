const caixas = document.getElementById("caixas");

function criar(tag, texto) {
    const elemento = document.createElement(tag);
    elemento.textContent = texto;
    return elemento;
}

async function carregarAvisos() {
    try {
        const resposta = await fetch("/api/avisos");
        const avisos = await resposta.json();

        avisos.forEach(function (aviso) {
            const card = document.createElement("div");
            card.className = "card";

            card.appendChild(criar("h2", aviso.titulo));
            card.appendChild(criar("p", "Data: " + aviso.data));

            if (aviso.descricao) {
                card.appendChild(criar("p", "Descrição: " + aviso.descricao));
            }

            const link = criar("a", "Ver mais");
            link.href = "aviso.html?id=" + aviso.id;
            card.appendChild(link);

            caixas.appendChild(card);
        });
    } catch (erro) {
        // Se o servidor estiver fora do ar, os avisos fixos continuam na página
        console.log("Não foi possível carregar os avisos novos.");
    }
}

carregarAvisos();