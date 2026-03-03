package org.example.api;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;
import io.javalin.Javalin;
import io.javalin.http.BadRequestResponse;
import org.example.config.StatusInfo;
import org.example.dto.TaskDTO;
import org.example.storage.TaskStorage;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.Map;

public class TaskApi {
    private final TaskStorage storage;
    private final ObjectMapper mapper = new ObjectMapper();

    public TaskApi(TaskStorage storage) {
        this.storage = storage;
        mapper.registerModule(new JavaTimeModule());
    }

    @SuppressWarnings("unchecked")
    public void setupRoutes(Javalin app) {

        app.get("/hello", ctx -> ctx.result("Hello, Javalin!"));

        app.get("/status", ctx -> {
            StatusInfo status = new StatusInfo("ok", LocalDateTime.now().format(DateTimeFormatter.ISO_LOCAL_DATE_TIME));
            ctx.json(status);
        });

        app.post("/echo", ctx -> {
            try {
                Map<String, Object> request = mapper.readValue(ctx.body(), Map.class);
                if (!request.containsKey("mensagem")) {
                    ctx.status(400).json(Map.of("erro", "O campo 'mensagem' é obrigatório"));
                    return;
                }
                ctx.status(201).json(Map.of("mensagem", request.get("mensagem")));
            } catch (JsonProcessingException e) {
                ctx.status(400).json(Map.of("erro", "JSON invalido: " + e.getMessage()));
            } catch (Exception e) {
                ctx.status(500).json(Map.of("erro", "Erro interno: " + e.getMessage()));
            }
        });

        app.get("/saudacao/{nome}", ctx -> {
            String name = ctx.pathParam("nome");
            ctx.json(Map.of("mensagem", "Olá, " + name + "!"));
        });

        app.post("/tasks", ctx -> {
            try {
                System.out.println("Corpo da requisição POST /tasks: " + ctx.body());
                List<TaskDTO> tasks = mapper.readValue(ctx.body(), mapper.getTypeFactory().constructCollectionType(List.class, TaskDTO.class));
                if (tasks == null || tasks.isEmpty()) {
                    throw new BadRequestResponse("Nenhuma tarefa adicionada");
                }
                for (TaskDTO task : tasks) {
                    if (task.getTitulo() == null || task.getTitulo().isBlank()) {
                        throw new BadRequestResponse("Todas as tarefas devem ter um titulo valido");
                    }
                    storage.addTask(task);
                }
                ctx.status(201).json(tasks);
            } catch (JsonProcessingException e) {
                System.err.println("Erro ao processar lista de tarefas: " + e.getMessage());
                e.printStackTrace();
                try {
                    TaskDTO task = ctx.bodyValidator(TaskDTO.class)
                            .check(t -> t.getTitulo() != null && !t.getTitulo().isBlank(), "Título é obrigatorio")
                            .check(t -> t.getDescricao() != null, "Descrição é obrigatória")
                            .get();
                    storage.addTask(task);
                    ctx.status(201).json(task);
                } catch (BadRequestResponse ex) {
                    System.err.println("Erro ao processar tarefa unica: " + ex.getMessage());
                    ctx.status(400).json(Map.of("erro", "Requisição invalida: " + ex.getMessage()));
                }
            } catch (Exception e) {
                System.err.println("Erro inesperado: " + e.getMessage());
                e.printStackTrace();
                ctx.status(500).json(Map.of("erro", "Erro interno do servidor: " + e.getMessage()));
            }
        });

        app.get("/tasks", ctx -> {
            String tasksJson = storage.getAllTasks();
            System.out.println("Tarefas retornadas GET /tasks: " + tasksJson);
            try {
                List<TaskDTO> tasks = mapper.readValue(tasksJson, mapper.getTypeFactory().constructCollectionType(List.class, TaskDTO.class));
                ctx.json(tasks);
            } catch (JsonProcessingException e) {
                ctx.status(500).json(Map.of("erro", "Erro ao desserializar tarefas: " + e.getMessage()));
            }
        });

        app.get("/tasks/{id}", ctx -> {
            try {
                int id = Integer.parseInt(ctx.pathParam("id"));
                String taskJson = storage.findTaskById(id);
                if (taskJson != null) {
                    ctx.json(mapper.readValue(taskJson, TaskDTO.class));
                } else {
                    ctx.status(404).json(Map.of("erro", "Tarefa não encontrada"));
                }
            } catch (NumberFormatException e) {
                ctx.status(400).json(Map.of("erro", "Formato de ID invAlido"));
            } catch (JsonProcessingException e) {
                ctx.status(500).json(Map.of("erro", "Erro ao desserializar tarefa: " + e.getMessage()));
            }
        });
    }
}