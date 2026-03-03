package org.example;
import io.javalin.Javalin;
import org.example.api.TaskApi;
import org.example.storage.TaskStorage;

public class Application {
    public static void main(String[] args) {
        TaskStorage storage = new TaskStorage();
        Javalin app = Javalin.create().start(7000);
        TaskApi api = new TaskApi(storage);
        api.setupRoutes(app);
    }
}
