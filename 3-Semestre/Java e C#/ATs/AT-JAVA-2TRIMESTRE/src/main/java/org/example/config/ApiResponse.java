package org.example.config;

public class ApiResponse {
    private final int statusCode;
    private final String content;

    public ApiResponse(int statusCode, String content) {
        this.statusCode = statusCode;
        this.content = content;
    }

    public int getStatusCode() {return statusCode;}
    public String getContent() {return content;}
}