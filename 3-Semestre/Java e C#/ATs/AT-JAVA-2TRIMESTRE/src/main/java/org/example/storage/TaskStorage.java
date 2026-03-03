package org.example.storage;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.example.dto.TaskDTO;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class TaskStorage {
    private final String dbUrl = "jdbc:sqlite:tasks.db";
    private final ObjectMapper mapper = new ObjectMapper();

    public TaskStorage() {
        try (Connection conn = DriverManager.getConnection(dbUrl)) {
            Statement stmt = conn.createStatement();
            stmt.execute("CREATE TABLE IF NOT EXISTS tasks (" +
                    "id INTEGER PRIMARY KEY AUTOINCREMENT," +
                    "titulo TEXT NOT NULL," +
                    "descricao TEXT NOT NULL," +
                    "concluida BOOLEAN NOT NULL," +
                    "dataCriacao TEXT NOT NULL)");
        } catch (SQLException e) {
            throw new RuntimeException("Erro ao criar a tabela: " + e.getMessage());
        }
    }

    public void addTask(TaskDTO task) {
        try (Connection conn = DriverManager.getConnection(dbUrl)) {
            PreparedStatement pstmt = conn.prepareStatement("INSERT INTO tasks (titulo, descricao, concluida, dataCriacao) VALUES (?, ?, ?, ?)");
            pstmt.setString(1, task.getTitulo());
            pstmt.setString(2, task.getDescricao());
            pstmt.setBoolean(3, task.isConcluida());
            pstmt.setString(4, task.getDataCriacao());
            pstmt.executeUpdate();
        } catch (SQLException e) {
            throw new RuntimeException("Erro ao adicionar tarefa: " + e.getMessage());
        }
    }

    public String findTaskById(int id) {
        try (Connection conn = DriverManager.getConnection(dbUrl)) {
            PreparedStatement pstmt = conn.prepareStatement("SELECT * FROM tasks WHERE id = ?");
            pstmt.setInt(1, id);
            ResultSet rs = pstmt.executeQuery();
            if (rs.next()) {
                TaskDTO task = new TaskDTO();
                task.setId(rs.getInt("id"));
                task.setTitulo(rs.getString("titulo"));
                task.setDescricao(rs.getString("descricao"));
                task.setConcluida(rs.getBoolean("concluida"));
                task.setDataCriacao(rs.getString("dataCriacao"));
                return mapper.writeValueAsString(task);
            }
            return null;
        } catch (SQLException e) {
            throw new RuntimeException("Erro ao buscar tarefa: " + e.getMessage());
        }
    }

    public String getAllTasks() {
        List<TaskDTO> tasks = new ArrayList<>();
        try (Connection conn = DriverManager.getConnection(dbUrl)) {
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM tasks");
            while (rs.next()) {
                TaskDTO task = new TaskDTO();
                task.setId(rs.getInt("id"));
                task.setTitulo(rs.getString("titulo"));
                task.setDescricao(rs.getString("descricao"));
                task.setConcluida(rs.getBoolean("concluida"));
                task.setDataCriacao(rs.getString("dataCriacao"));
                tasks.add(task);
            }
            return mapper.writeValueAsString(tasks);
        } catch (SQLException e) {
            throw new RuntimeException("Erro ao listar tarefas: " + e.getMessage());
        }
    }
}