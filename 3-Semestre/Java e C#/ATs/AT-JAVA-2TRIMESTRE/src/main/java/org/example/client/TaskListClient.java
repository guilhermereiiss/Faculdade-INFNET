package org.example.client;
import org.example.config.ApiResponse;
import org.example.dto.TaskDTO;
import java.io.IOException;
import java.net.URISyntaxException;

public class TaskListClient {
    public void listTasks() throws IOException, URISyntaxException {
        String url = "http://localhost:7000/tasks";
        for (int i = 0; i < 3; i++) {
            TaskDTO task = new TaskDTO("Task " + (i + 1), "Description " + (i + 1), false);
            HttpClientUtil.post(url, task);
        }
        ApiResponse response = HttpClientUtil.get(url);
        System.out.println("List Tasks Response: " + response.getContent());
    }
}