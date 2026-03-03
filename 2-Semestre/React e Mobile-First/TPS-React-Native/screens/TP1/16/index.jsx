import React from 'react';
import { StyleSheet, Text, View, ScrollView } from 'react-native';

const App = () => {
  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>Estrutura de um App React Native</Text>
      <Text style={styles.paragraph}>
        A estrutura de um app React Native é crucial para desenvolver apps móveis de alta qualidade. Criado pelo Facebook, o React Native possibilita aos desenvolvedores a utilização de JavaScript e React para desenvolver aplicativos com uma experiência nativa.
      </Text>
      <Text style={styles.paragraph}>
        A arquitetura possui três camadas principais: Camada de Interface do Usuário, Camada de Lógica de Negócios e Camada de Integração Nativa. A primeira utiliza componentes React organizados em uma árvore para construir uma interface com base no estado da aplicação.

        A segunda gerencia o estado e a comunicação entre componentes, frequentemente utilizando Redux ou Context API. A terceira permite a interação com componentes nativos do dispositivo, como câmeras e GPS, por meio de uma ponte que conecta o código JavaScript aos componentes nativos.
      </Text>
      <Text style={styles.paragraph}>
        Comparado com o React, que mostra componentes em um DOM para apps web, o React Native exibe componentes nativos, proporcionando uma experiência mais integrada e eficaz. Esta estrutura proporciona a maleabilidade do React com a habilidade de utilizar elementos nativos, gerando aplicativos móveis e velozes.
      </Text>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    padding: 16,
    backgroundColor: '#f5f5f5',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 16,
    color: '#333',
  },
  paragraph: {
    fontSize: 16,
    lineHeight: 24,
    marginBottom: 12,
    color: '#666',
  },
});

export default App;
