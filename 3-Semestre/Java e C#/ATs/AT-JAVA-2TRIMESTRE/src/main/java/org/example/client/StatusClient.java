package org.example.client;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.example.config.ApiResponse;
import java.io.IOException;
import java.net.URISyntaxException;
import java.util.Map;

public class StatusClient {
    private static final ObjectMapper mapper = new ObjectMapper();

    public void getStatus() throws IOException, URISyntaxException {
        String url = "http://localhost:7000/status";
        ApiResponse response = HttpClientUtil.get(url);
        Map<String, Object> responseMap = mapper.readValue(response.getContent(), Map.class);
        String formattedResponse = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(responseMap);
        System.out.println("Status Response:\n" + formattedResponse);
    }
}