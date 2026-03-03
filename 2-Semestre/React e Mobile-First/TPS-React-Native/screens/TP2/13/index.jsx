import { useState } from 'react';
import Question from './components/Question.jsx';
import Result from './components/Result.jsx';
import { View, Button } from 'react-native';
import QuestionsData from "./data/questions.json";
import Style from "./styles.jsx";

function App() {
    const [currentQuestion, setCurrentQuestion] = useState(0);
    const [score, setScore] = useState(0);
    const [view, setView] = useState('question');
    const [quizCompleted, setQuizCompleted] = useState(false);

    const handleAnswer = (answer) => {
        if (answer === QuestionsData[currentQuestion].answer) {
            setScore(score + 1);
        }
        const nextQuestion = currentQuestion + 1;
        if (nextQuestion < QuestionsData.length) {
            setCurrentQuestion(nextQuestion);
        } else {
            setQuizCompleted(true);
            setView('result');
        }
    };

    const handleNavigation = (view) => {
        setView(view);
    };

    return (
        <View style={Style.app}>
            <View style={{ flexDirection: 'row', marginBottom: 20 }}>
                <Button title="Questões" onPress={() => handleNavigation('question')} />
                <Button title="Resultado" onPress={() => handleNavigation('result')} />
            </View>
            {view === 'question' && !quizCompleted && (
                <Question
                    question={QuestionsData[currentQuestion]}
                    handleAnswer={handleAnswer}
                />
            )}
            {view === 'result' && (
                <Result score={score} total={QuestionsData.length} />
            )}
        </View>
    );
}

export default App;
