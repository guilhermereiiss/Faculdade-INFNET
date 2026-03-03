import { useState } from "react";
import "./styles.css";

const questoes = [
    {
      enunciado: "O que é Mobile-First?",
      opcoes: [
        "A. Design para desktop",
        "B. Design responsivo",
        "C. Design para mobile",
        "D. Design para tablet"
      ],
      correta: "C. Design para mobile",
      justificativa:
        "Mobile-First é a abordagem de design que começa com dispositivos móveis, adaptando-se posteriormente para telas maiores."
    },
    {
      enunciado: "O que é responsividade no design?",
      opcoes: [
        "A. Usar imagens grandes",
        "B. Criar diferentes layouts para cada dispositivo",
        "C. Ajustar o layout de acordo com o tamanho da tela do dispositivo",
        "D. Focar apenas em mobile"
      ],
      correta: "C. Ajustar o layout de acordo com o tamanho da tela do dispositivo",
      justificativa:
        "Responsividade permite que o design se adapte a diferentes tamanhos de tela."
    },
    {
      enunciado: "Qual a vantagem de usar 'em' ou 'rem' em vez de 'px' no CSS?",
      opcoes: [
        "A. Melhora a performance",
        "B. Facilita a escalabilidade do layout",
        "C. São mais precisos",
        "D. Não há diferença"
      ],
      correta: "B. Facilita a escalabilidade do layout",
      justificativa:
        "'em' e 'rem' são unidades relativas que permitem uma melhor escalabilidade em layouts responsivos."
    },
    {
      enunciado: "O que o atributo 'viewport' faz no HTML?",
      opcoes: [
        "A. Ajusta o layout para telas maiores",
        "B. Define o espaço visível para a página",
        "C. Otimiza o tempo de carregamento",
        "D. Nada"
      ],
      correta: "B. Define o espaço visível para a página",
      justificativa:
        "O atributo 'viewport' define como o conteúdo da página é escalado e exibido em diferentes dispositivos."
    },
    {
      enunciado: "Qual abordagem facilita a manutenção de código para diferentes telas?",
      opcoes: [
        "A. Tabelas",
        "B. Grid fixo",
        "C. Media Queries",
        "D. Layout fluido"
      ],
      correta: "C. Media Queries",
      justificativa:
        "Media Queries permitem aplicar estilos diferentes com base em características específicas do dispositivo, como largura de tela."
    },
    {
      enunciado: "O que 'min-width' significa em uma Media Query?",
      opcoes: [
        "A. Aplicar o estilo em telas maiores que um valor mínimo",
        "B. Aplicar o estilo em telas menores que um valor mínimo",
        "C. Definir o tamanho mínimo do elemento",
        "D. Bloquear o estilo em telas pequenas"
      ],
      correta: "A. Aplicar o estilo em telas maiores que um valor mínimo",
      justificativa:
        "Usar 'min-width' permite aplicar estilos em telas maiores que o valor definido, útil na abordagem Mobile-First."
    },
    {
      enunciado: "Qual é o propósito de 'flexbox' no layout responsivo?",
      opcoes: [
        "A. Criar um layout fixo",
        "B. Alinhar itens de forma flexível",
        "C. Forçar o uso de margens",
        "D. Substituir CSS Grid"
      ],
      correta: "B. Alinhar itens de forma flexível",
      justificativa:
        "Flexbox é uma técnica usada para alinhar e distribuir elementos de melhor forma em layouts responsivos."
    },
    {
      enunciado: "O que 'usabilidade' significa no design web?",
      opcoes: [
        "A. Acessibilidade do site",
        "B. Como o design facilita a interação do usuário",
        "C. Velocidade de carregamento",
        "D. Design apenas para mobile"
      ],
      correta: "B. Como o design facilita a interação do usuário",
      justificativa:
        "Usabilidade refere-se à facilidade com que os usuários podem interagir com um site ou aplicativo."
    },
    {
      enunciado: "Qual técnica melhora a acessibilidade em sites responsivos?",
      opcoes: [
        "A. Contraste adequado de cores",
        "B. Usar fontes pequenas",
        "C. Remover imagens",
        "D. Usar apenas JavaScript"
      ],
      correta: "A. Contraste adequado de cores",
      justificativa:
        "Contraste adequado entre cores é essencial para que pessoas com deficiências visuais possam usar o site de maneira eficaz."
    },
    {
      enunciado: "Qual a resolução mínima mais comum para o design Mobile-First?",
      opcoes: [
        "A. 320px",
        "B. 768px",
        "C. 1024px",
        "D. 1440px"
      ],
      correta: "A. 320px",
      justificativa:
        "320px é frequentemente usada como resolução mínima ao projetar para dispositivos móveis na abordagem Mobile-First."
    }
  ];
  

const Quiz = () => {
  const [indiceAtual, setIndiceAtual] = useState(0);
  const [respostaSelecionada, setRespostaSelecionada] = useState(null);
  const [confirmada, setConfirmada] = useState(false);
  const [pontuacao, setPontuacao] = useState(0);

  const questaoAtual = questoes[indiceAtual];

  const selecionarResposta = (opcao) => {
    setRespostaSelecionada(opcao);
  };

  const confirmarResposta = () => {
    if (respostaSelecionada) {
      setConfirmada(true);
      if (respostaSelecionada === questaoAtual.correta) {
        setPontuacao(pontuacao + 1);
      }
    }
  };

  const proximaQuestao = () => {
    setIndiceAtual(indiceAtual + 1);
    setConfirmada(false);
    setRespostaSelecionada(null);
  };

  return (
    <div className="quiz-container">
      {indiceAtual < questoes.length ? (
        <>
          <h2>{questaoAtual.enunciado}</h2>
          <div className="opcoes">
            {questaoAtual.opcoes.map((opcao, index) => (
              <button
                key={index}
                onClick={() => selecionarResposta(opcao)}
                className={respostaSelecionada === opcao ? "selecionada" : ""}
              >
                {opcao}
              </button>
            ))}
          </div>
          {!confirmada ? (
            <button onClick={confirmarResposta}>Confirmar</button>
          ) : (
            <div>
              <p>{respostaSelecionada === questaoAtual.correta ? "Correto!" : "Incorreto!"}</p>
              <p>{questaoAtual.justificativa}</p>
              <button onClick={proximaQuestao}>Próxima</button>
            </div>
          )}
        </>
      ) : (
        <div className="resultado">
          <h2>Você acertou {pontuacao} de {questoes.length} questões!</h2>
        </div>
      )}
    </div>
  );
};

export default Quiz;
