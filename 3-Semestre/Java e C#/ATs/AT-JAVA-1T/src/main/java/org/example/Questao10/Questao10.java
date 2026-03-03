package org.example.Questao10;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.FileAlreadyExistsException;
import java.nio.file.Files;
import java.io.*;
import java.util.Scanner;

public class Questao10 {
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String arquivo = "compras.txt";

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(arquivo))) {
            for (int i = 1; i <= 3; i++) {
                System.out.println("Cadastro das compras " + i + ":");
                System.out.print("Produto: ");
                String produto = scanner.nextLine();
                System.out.print("Quantidade: ");
                int quantidade = Integer.parseInt(scanner.nextLine());
                System.out.print("Preço: ");
                double preco = Double.parseDouble(scanner.nextLine());
                System.out.println();

                writer.write(produto + ", " + quantidade + ", " + preco);
                writer.newLine();
            }
            System.out.println("Compras registradas!!!!");
        } catch (IOException e) {
            System.out.println("Erro ao escrever no arquivo: " + e.getMessage());
        }
        System.out.println("\nCompras Registradas:");
        try (BufferedReader reader = new BufferedReader(new FileReader(arquivo))) {
            String linha;
            while ((linha = reader.readLine()) != null) {
                System.out.println(linha);
            }
        } catch (IOException e) {
            System.out.println("Erro ao ler o seu arquivo: " + e.getMessage());
        }
        scanner.close();
    }
}
