import { View, Text, StatusBar, StyleSheet, Linking } from 'react-native';

export default function Home() {
  return (
    <View>
        <Text style={style.Title}>Template de React Native.</Text>
        <View>
          <Text style={style.subTitle}>Guia rápido.</Text>
          <Text style={style.paragraph}>npm install para instalar as dependencias necessárias.</Text>
          <Text style={style.paragraph}>npx expo start para acessar na Web, Android ou IOS.</Text>
          <Text style={style.paragraph}>Os exercícios estão no Menu abaixo para a visualização.</Text>
          <Text style={style.paragraph}>No Projeto, cada TP está dividido em pastas, portanto tome cuidado com a linkagem! Recomendo olhar <Text style={style.link} onPress={() => Linking.openURL("https://reactnavigation.org/docs/getting-started/")}>Documentação</Text> caso tenha duvida!</Text>
          <Text style={style.paragraph}>Nota: Caso deseje exportar pro Snack, lembre-se de sempre fazer importação explícita.</Text>
          <Text style={style.paragraph}>Exemplo: import Component from "./Folder/index.js"</Text>
          <Text style={style.footer}>Bons TPs!</Text>
        </View>
        <StatusBar />
    </View>
  );
}

const style = StyleSheet.create({
  Title: {
    fontSize: 20,
    fontWeight: "bold",
    textAlign: "center",
    marginTop: 25
  },
  subTitle: {
    fontSize: 15,
    fontWeight: "bold",
    marginTop: 15,
    textAlign: "center"
  },
  paragraph: {
    fontSize: 15,
    marginTop: 10,
    marginLeft: 10,
    marginRight: 10
  },
  link: {
    color: "#007FFF"
  },
  footer: {
    fontSize: 15,
    marginTop: 10,
    textAlign: "center"
  }
});