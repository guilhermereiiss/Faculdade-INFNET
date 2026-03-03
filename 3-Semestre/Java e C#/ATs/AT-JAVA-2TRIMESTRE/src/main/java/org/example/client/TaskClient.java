package org.example.client;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.example.config.ApiResponse;
import org.example.dto.TaskDTO;
import java.io.IOException;
import java.net.URISyntaxException;
import java.util.Map;

public class TaskClient {
    private static final ObjectMapper mapper = new ObjectMapper();

    public void createTask() throws IOException, URISyntaxException {
        String url = "http://localhost:7000/tasks";
        TaskDTO task = new TaskDTO("New Task", "Task Description", false);
        ApiResponse response = HttpClientUtil.post(url, task);
        Map<String, Object> responseMap = mapper.readValue(response.getContent(), Map.class);
        String formattedResponse = mapper.writerWithDefaultPrettyPrinter().writeValueAsString(responseMap);
        System.out.println("Create Task Response:\n" + formattedResponse);
    }
}