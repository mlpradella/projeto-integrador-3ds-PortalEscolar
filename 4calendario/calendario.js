// Substitua estas duas funções no seu <script>:

async function carregarCalendario() {
    try {
        const resposta = await fetch('http://localhost:5000/api/calendario');
        const dados = await resposta.json();

        document.getElementById('titulo-mes').innerText = `Calendário de ${dados.mes}`;
        eventosGlobais = dados.eventos || {};

        for (let i = 1; i <= dados.dias_no_mes; i++) {
            const divDia = document.getElementById(`dia-${i}`);
            if (divDia) {
                let conteudo = `<span>${i}</span>`;
                
                // Procura tanto por inteiro (i) como por string (String(i))
                const eventosDoDia = eventosGlobais[i] || eventosGlobais[String(i)];
                
                if (eventosDoDia && eventosDoDia.length > 0) {
                    divDia.classList.add('com-evento');
                    const listaEventos = eventosDoDia
                        .map(evento => `<small class="descricao-evento">${evento}</small>`)
                        .join('');
                    conteudo += listaEventos;
                }
                
                divDia.innerHTML = conteudo;
            }
        }
    } catch (erro) {
        console.log('Servidor offline. Exibindo calendário estático.');
    }
}

function verDetalhesDia(dia) {
    const modal = document.getElementById('modal-detalhes');
    const titulo = document.getElementById('modal-titulo');
    const lista = document.getElementById('modal-lista-eventos');

    titulo.innerText = `Informações do Dia ${dia} de Julho`;
    lista.innerHTML = '';

    // Procura o dia como número ou como texto na variável de memória
    const eventosDoDia = eventosGlobais[dia] || eventosGlobais[String(dia)];

    if (eventosDoDia && eventosDoDia.length > 0) {
        eventosDoDia.forEach(evento => {
            const li = document.createElement('li');
            li.innerText = evento;
            lista.appendChild(li);
        });
    } else {
        const li = document.createElement('li');
        li.innerText = 'Nenhum aviso ou prova cadastrada para este dia.';
        lista.appendChild(li);
    }

    modal.style.display = 'flex';
}