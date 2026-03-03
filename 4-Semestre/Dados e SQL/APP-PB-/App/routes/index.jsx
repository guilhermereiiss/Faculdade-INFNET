import { NavigationContainer } from "@react-navigation/native";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { Ionicons, FontAwesome } from '@expo/vector-icons'; 
import HomeScreen from "../views/Home/index.jsx";
import FilmeScreen from "../views/Filmes/index.jsx";
import FavoritosScreen from "../views/Favoritos/index.jsx";

const Tab = createBottomTabNavigator();
const cores = {
    corPrimaria: '#ffffff',
    corSecundaria: '#281259',
    corBotao: '#9F2CBF',
    corBotaoTexto: '#ffffff',
    sombraCard: '#d9d9d9', 
};

export default function Routes() {
    return (
        <NavigationContainer>
            <Tab.Navigator
                screenOptions={{
                    tabBarActiveTintColor: cores.corBotao,
                    tabBarInactiveTintColor: cores.corSecundaria,
                    tabBarStyle: {
                        backgroundColor: cores.corPrimaria,
                        borderTopColor: cores.sombraCard,
                    },
                    headerStyle: {
                        backgroundColor: cores.corSecundaria,
                    },
                    headerTintColor: cores.corBotaoTexto,
                }}
            >
                <Tab.Screen
                    name="MatchMovie"
                    component={HomeScreen}
                    options={{
                        tabBarIcon: ({ color, size }) => (
                            <FontAwesome name="home" color={color} size={size} />
                        ),
                    }}
                />
                <Tab.Screen
                    name="Filmes"
                    component={FilmeScreen}
                    options={{
                        tabBarIcon: ({ color, size }) => (
                            <FontAwesome name="film" color={color} size={size} />
                        ),
                    }}
                />
                <Tab.Screen
                    name="Favoritos"
                    component={FavoritosScreen}
                    options={{
                        tabBarIcon: ({ color, size }) => (
                            <FontAwesome name="star" color={color} size={size} />
                        ),
                    }}
                    initialParams={{ favoritos: [] }} 
                />

            </Tab.Navigator>
        </NavigationContainer>
    );
}
