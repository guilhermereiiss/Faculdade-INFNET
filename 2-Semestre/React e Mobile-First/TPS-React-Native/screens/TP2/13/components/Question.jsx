import { View, Text, Button } from "react-native";
import styles from "../styles.jsx";

function Question({ question, handleAnswer, disabled }) {
  if (!question || !question.options) {
    return <Text>Dados da pergunta não carregados corretamente.</Text>;
  }

  return (
    <View style={styles.questionContainer}>
      <Text style={styles.questionText}>{question.question}</Text>
      <View style={styles.optionsButton}>
        {question.options.map((option, index) => (
          <View key={index} style={styles.optionsText}>
            <Button
              title={option}
              onPress={() => handleAnswer(option)}
              color={disabled ? "gray" : "black"} 
              disabled={disabled} 
            />
          </View>
        ))}
      </View>
    </View>
  );
}

export default Question;
