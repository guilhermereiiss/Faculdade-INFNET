package org.example.api;
import io.javalin.Javalin;
import io.javalin.http.HttpStatus;
import org.example.storage.TaskStorage;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import static org.junit.jupiter.api.Assertions.*;

public class TaskApiTest {
    private static Javalin app;
    private static final String BASE_URL = "http://localhost:7000";

    @BeforeEach
    public void setUp() {
        TaskStorage storage = new TaskStorage();
        TaskApi taskApi = new TaskApi(storage);
        app = Javalin.create().start(7000);
        taskApi.setupRoutes(app);
    }

    @AfterEach
    public void tearDown() {
        if (app != null) {
            app.stop();
        }
    }

    @Test
    public void testHelloEndpoint() throws Exception {
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/hello"))
                .GET()
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        assertEquals(HttpStatus.OK.getCode(), response.statusCode());
        assertEquals("Hello, Javalin!", response.body());
    }

    @Test
    public void testCreateTaskEndpoint() throws Exception {
        HttpClient client = HttpClient.newHttpClient();
        String requestBody = "{\"titulo\": \"Teste do Guizinho\", \"descricao\": \"100% no AT\", \"concluida\": true}";
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/tasks"))
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(requestBody))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        assertEquals(HttpStatus.CREATED.getCode(), response.statusCode());
        assertTrue(response.body().contains("\"titulo\":\"Teste do Guizinho\""));
    }

    @Test
    public void testGetTaskByIdEndpoint() throws Exception {
        HttpClient client = HttpClient.newHttpClient();
        String requestBody = "{\"titulo\": \"Teste do Guizinho\", \"descricao\": \"100% no AT\", \"concluida\": false}";
        HttpRequest postRequest = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/tasks"))
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(requestBody))
                .build();
        client.send(postRequest, HttpResponse.BodyHandlers.ofString());

        Thread.sleep(100);
        HttpRequest getRequest = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/tasks/1"))
                .GET()
                .build();

        HttpResponse<String> response = client.send(getRequest, HttpResponse.BodyHandlers.ofString());
        assertEquals(HttpStatus.OK.getCode(), response.statusCode());
        assertTrue(response.body().contains("\"titulo\":\"Teste do Guizinho\""));
    }

    @Test
    public void testGetAllTasksEndpoint() throws Exception {
        HttpClient client = HttpClient.newHttpClient();
        String requestBody = "{\"titulo\": \"Teste do Neymar\", \"descricao\": \"100% no AT\", \"concluida\": false}";
        HttpRequest postRequest = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/tasks"))
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(requestBody))
                .build();
        client.send(postRequest, HttpResponse.BodyHandlers.ofString());

        Thread.sleep(100);
        HttpRequest getRequest = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/tasks"))
                .GET()
                .build();

        HttpResponse<String> response = client.send(getRequest, HttpResponse.BodyHandlers.ofString());
        assertEquals(HttpStatus.OK.getCode(), response.statusCode());
        assertTrue(response.body().contains("\"titulo\":\"Teste do Neymar\""));
        assertFalse(response.body().equals("[]"));
    }
}