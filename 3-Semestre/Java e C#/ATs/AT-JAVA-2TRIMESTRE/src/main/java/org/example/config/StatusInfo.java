package org.example.config;

public class StatusInfo {
    private String status;
    private String timestamp;

    public StatusInfo(String status, String timestamp) {
        this.status = status;
        this.timestamp = timestamp;
    }

    public String getStatus() {
        return status;
    }

    public String getTimestamp() {
        return timestamp;
    }
}