package org.example.api;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;

public class ApiClient {
    private static final String BASE_URL = "http://localhost:7000";

    public static void createTask() {
        try {
            URL url = new URL(BASE_URL + "/tasks");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("Content-Type", "application/json; charset=UTF-8");
            connection.setDoOutput(true);

            String jsonInput = "{\"titulo\": \"Feijoada\", \"descricao\": \"Descrição da Feijoada\", \"concluida\": false}";
            try (OutputStream os = connection.getOutputStream()) {
                os.write(jsonInput.getBytes(StandardCharsets.UTF_8));
            }

            int responseCode = connection.getResponseCode();
            System.out.println("Código (Criar Tarefa): " + responseCode);
            if (responseCode == HttpURLConnection.HTTP_CREATED) {
                try (BufferedReader reader = new BufferedReader(
                        new InputStreamReader(connection.getInputStream(), StandardCharsets.UTF_8))) {
                    System.out.println("Resposta: " + reader.readLine());
                }
            } else {
                System.out.println("Falha ao criar tarefa.");
            }
            connection.disconnect();
        } catch (Exception e) {
            System.err.println("Erro: " + e.getMessage());
        }
    }

    public static void listTasks() {
        try {
            URL url = new URL(BASE_URL + "/tasks");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Accept", "application/json");

            int responseCode = connection.getResponseCode();
            System.out.println("Código (Listar Tarefas): " + responseCode);
            if (responseCode == HttpURLConnection.HTTP_OK) {
                try (BufferedReader reader = new BufferedReader(
                        new InputStreamReader(connection.getInputStream(), StandardCharsets.UTF_8))) {
                    System.out.println("Resposta: " + reader.readLine());
                }
            } else {
                System.out.println("Falha ao listar tarefas.");
            }
            connection.disconnect();
        } catch (Exception e) {
            System.err.println("Erro: " + e.getMessage());
        }
    }

    public static void getTaskById(int id) {
        try {
            URL url = new URL(BASE_URL + "/tasks/" + id);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Accept", "application/json");

            int responseCode = connection.getResponseCode();
            System.out.println("Código (Buscar por ID): " + responseCode);
            if (responseCode == HttpURLConnection.HTTP_OK) {
                try (BufferedReader reader = new BufferedReader(
                        new InputStreamReader(connection.getInputStream(), StandardCharsets.UTF_8))) {
                    System.out.println("Resposta: " + reader.readLine());
                }
            } else {
                System.out.println("Tarefa não encontrada.");
            }
            connection.disconnect();
        } catch (Exception e) {
            System.err.println("Erro: " + e.getMessage());
        }
    }

    public static void getStatus() {
        try {
            URL url = new URL(BASE_URL + "/status");
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Accept", "application/json");

            int responseCode = connection.getResponseCode();
            System.out.println("Código (Status): " + responseCode);
            if (responseCode == HttpURLConnection.HTTP_OK) {
                try (BufferedReader reader = new BufferedReader(
                        new InputStreamReader(connection.getInputStream(), StandardCharsets.UTF_8))) {
                    System.out.println("Resposta: " + reader.readLine());
                }
            } else {
                System.out.println("Falha ao obter status.");
            }
            connection.disconnect();
        } catch (Exception e) {
            System.err.println("Erro: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        System.out.println("Criando tarefa...");
        createTask();

        System.out.println("\nListando tarefas...");
        listTasks();

        System.out.println("\nBuscando tarefa ID 1...");
        getTaskById(1);

        System.out.println("\nObtendo status...");
        getStatus();
    }
}