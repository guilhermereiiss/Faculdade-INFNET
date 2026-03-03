package org.example.client;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.example.config.ApiResponse;
import org.example.dto.TaskDTO;
import java.io.IOException;
import java.net.URISyntaxException;
import java.util.Map;

public class TaskByIdClient {
    private static final ObjectMapper mapper = new ObjectMapper();

    public void getTaskById() throws IOException, URISyntaxException {
        String url = "http://localhost:7000/tasks";
        for (int i = 0; i < 3; i++) {
            TaskDTO task = new TaskDTO("Task " + (i + 1), "Description " + (i + 1), false);
            HttpClientUtil.post(url, task);
        }
        int id = (int) (Math.random() * 3) + 1;
        ApiResponse response = HttpClientUtil.get(url + "/" + id);
        Map<String, Object> responseMap = mapper.readValue(response.getContent(), Map.class);
        String formattedResponse = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(responseMap);
        System.out.println("Get Task by ID Response:\n" + formattedResponse);
    }
}
