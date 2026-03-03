import { useState } from "react";
import { View, Text, TouchableOpacity, StyleSheet } from "react-native";

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
      enunciado: "Em 'Naruto', qual é o nome da vila onde Naruto vive?",
      opcoes: [
        "A. Vila da Folha",
        "B. Vila da Areia",
        "C. Vila da Névoa",
        "D. Vila do Som"
      ],
      correta: "A. Vila da Folha",
      justificativa:
        "Naruto vive na Vila Oculta da Folha, também conhecida como Konoha."
    },
    {
      enunciado: "Qual destes animes foi criado por Akira Toriyama?",
      opcoes: [
        "A. One Piece",
        "B. Dragon Ball",
        "C. Naruto",
        "D. Bleach"
      ],
      correta: "B. Dragon Ball",
      justificativa:
        "Akira Toriyama é o famoso criador de Dragon Ball, um dos animes mais populares do mundo."
    },
    {
      enunciado: "Em 'Attack on Titan', qual é o nome da cidade onde a história começa?",
      opcoes: [
        "A. Wall Maria",
        "B. Shiganshina",
        "C. Trost",
        "D. Marley"
      ],
      correta: "B. Shiganshina",
      justificativa:
        "Shiganshina é o distrito onde a história de Attack on Titan começa, localizado ao lado da Muralha Maria."
    },
    {
      enunciado: "Qual seleção venceu a Copa do Mundo da FIFA em 2018?",
      opcoes: [
        "A. Alemanha",
        "B. Brasil",
        "C. França",
        "D. Argentina"
      ],
      correta: "C. França",
      justificativa:
        "A França venceu a Copa do Mundo de 2018, realizada na Rússia, ao derrotar a Croácia na final."
    },
    {
      enunciado: "Qual jogador é conhecido como 'El Fenômeno' no mundo do futebol?",
      opcoes: [
        "A. Lionel Messi",
        "B. Ronaldo Nazário",
        "C. Cristiano Ronaldo",
        "D. Ronaldinho Gaúcho"
      ],
      correta: "B. Ronaldo Nazário",
      justificativa:
        "Ronaldo Nazário, ex-jogador brasileiro, é conhecido como 'El Fenômeno' devido ao seu talento único no futebol."
    },
    {
      enunciado: "Qual time é conhecido como 'Rubro-Negro' no Brasil?",
      opcoes: [
        "A. Grêmio",
        "B. Flamengo",
        "C. Fluminense",
        "D. São Paulo"
      ],
      correta: "B. Flamengo",
      justificativa:
        "O Flamengo é chamado de 'Rubro-Negro' devido às suas cores vermelho e preto."
    },
    {
      enunciado: "Quem é o maior artilheiro da Seleção Brasileira de Futebol?",
      opcoes: [
        "A. Romário",
        "B. Pelé",
        "C. Ronaldo",
        "D. Neymar"
      ],
      correta: "B. Pelé",
      justificativa:
        "Pelé é o maior artilheiro da Seleção Brasileira, com mais de 70 gols marcados em jogos oficiais."
    }
  ];
  

const App = () => {
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
    <View style={styles.container}>
      {indiceAtual < questoes.length ? (
        <>
          <Text style={styles.enunciado}>{questaoAtual.enunciado}</Text>
          <View style={styles.opcoes}>
            {questaoAtual.opcoes.map((opcao, index) => (
              <TouchableOpacity
                key={index}
                onPress={() => selecionarResposta(opcao)}
                style={[
                  styles.opcao,
                  respostaSelecionada === opcao ? styles.selecionada : null
                ]}
              >
                <Text style={styles.textoOpcao}>{opcao}</Text>
              </TouchableOpacity>
            ))}
          </View>
          {!confirmada ? (
            <TouchableOpacity style={styles.botao} onPress={confirmarResposta}>
              <Text style={styles.textoBotao}>Confirmar</Text>
            </TouchableOpacity>
          ) : (
            <View style={styles.resultado}>
              <Text style={styles.feedback}>
                {respostaSelecionada === questaoAtual.correta
                  ? "Correto!"
                  : "Incorreto!"}
              </Text>
              <Text style={styles.justificativa}>{questaoAtual.justificativa}</Text>
              <TouchableOpacity style={styles.botao} onPress={proximaQuestao}>
                <Text style={styles.textoBotao}>Próxima</Text>
              </TouchableOpacity>
            </View>
          )}
        </>
      ) : (
        <View style={styles.resultadoFinal}>
          <Text style={styles.resultadoTexto}>
            Você acertou {pontuacao} de {questoes.length} questões!
          </Text>
        </View>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    padding: 20,
    backgroundColor: "#f0f0f5",
  },
  enunciado: {
    fontSize: 20,
    fontWeight: "bold",
    marginBottom: 20,
    color: "#333",
  },
  opcoes: {
    marginBottom: 20,
  },
  opcao: {
    padding: 15,
    borderRadius: 5,
    backgroundColor: "#e0e0e0",
    marginBottom: 10,
  },
  selecionada: {
    backgroundColor: "#b0e0e6",
  },
  textoOpcao: {
    fontSize: 18,
    color: "#333",
  },
  botao: {
    backgroundColor: "#4CAF50",
    padding: 15,
    borderRadius: 5,
    alignItems: "center",
    marginTop: 10,
  },
  textoBotao: {
    color: "#fff",
    fontSize: 16,
    fontWeight: "bold",
  },
  resultado: {
    alignItems: "center",
  },
  feedback: {
    fontSize: 18,
    fontWeight: "bold",
    color: "#333",
  },
  justificativa: {
    fontSize: 16,
    color: "#666",
    marginTop: 10,
    textAlign: "center",
  },
  resultadoFinal: {
    alignItems: "center",
  },
  resultadoTexto: {
    fontSize: 22,
    fontWeight: "bold",
    color: "#333",
  },
});

export default App;
