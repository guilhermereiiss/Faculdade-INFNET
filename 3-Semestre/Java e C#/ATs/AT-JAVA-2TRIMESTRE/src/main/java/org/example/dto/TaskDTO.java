package org.example.dto;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class TaskDTO {
    private int id;
    private String titulo;
    private String descricao;
    private boolean concluida;
    private String dataCriacao;

    public TaskDTO() {
    }

    public TaskDTO(String titulo, String descricao, boolean concluida) {
        this.titulo = titulo;
        this.descricao = descricao;
        this.concluida = concluida;
        this.dataCriacao = LocalDateTime.now().format(DateTimeFormatter.ISO_LOCAL_DATE_TIME);
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public boolean isConcluida() {
        return concluida;
    }

    public void setConcluida(boolean concluida) {
        this.concluida = concluida;
    }

    public String getDataCriacao() {
        return dataCriacao;
    }

    public void setDataCriacao(String dataCriacao) {
        this.dataCriacao = dataCriacao;
    }
}