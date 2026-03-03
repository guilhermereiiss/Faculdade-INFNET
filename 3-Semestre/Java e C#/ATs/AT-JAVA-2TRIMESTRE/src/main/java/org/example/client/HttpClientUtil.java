package org.example.client;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.example.config.ApiResponse;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;
import java.nio.charset.StandardCharsets;

public class HttpClientUtil {
    private static final ObjectMapper mapper = new ObjectMapper();

    public static ApiResponse get(String urlString) throws IOException, URISyntaxException {
        HttpURLConnection connection = createConnection(urlString, "GET");
        int status = connection.getResponseCode();
        String responseBody = readResponse(status < 400 ? connection.getInputStream() : connection.getErrorStream());
        if (status >= 400) {
            throw new IOException("GET Requisicao falhou. Status: " + status + ", Response: " + responseBody);
        }
        return new ApiResponse(status, responseBody);
    }

    public static ApiResponse post(String urlString, Object body) throws IOException, URISyntaxException {
        HttpURLConnection connection = createConnection(urlString, "POST");
        connection.setRequestProperty("Content-Type", "application/json; charset=UTF-8");

        String jsonInput = mapper.writeValueAsString(body);
        try (OutputStream os = connection.getOutputStream()) {
            os.write(jsonInput.getBytes(StandardCharsets.UTF_8));
        }

        int status = connection.getResponseCode();
        String responseBody = readResponse(status < 400 ? connection.getInputStream() : connection.getErrorStream());
        if (status != 200 && status != 201) {
            throw new IOException("POST Requisicao falhou. Status: " + status + ", Response: " + responseBody);
        }
        return new ApiResponse(status, responseBody);
    }

    private static HttpURLConnection createConnection(String urlString, String method) throws IOException, URISyntaxException {
        URL url = new URI(urlString).toURL();
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setRequestMethod(method);
        connection.setRequestProperty("Accept", "application/json");
        if ("POST".equals(method)) {
            connection.setDoOutput(true);
        }
        return connection;
    }

    private static String readResponse(java.io.InputStream stream) throws IOException {
        if (stream == null) return "";
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(stream, StandardCharsets.UTF_8))) {
            StringBuilder response = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                response.append(line).append('\n');
            }
            return response.toString().trim();
        }
    }
}