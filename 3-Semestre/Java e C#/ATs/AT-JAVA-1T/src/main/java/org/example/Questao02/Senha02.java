package org.example.Questao02;
import java.util.Scanner;
import java.util.regex.Pattern;

public class Senha02 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite seu nome: ");
        String nome = scanner.nextLine();
        String senha;

        while (true) {
            System.out.print("Digite sua senha: ");
            senha = scanner.nextLine();

            String mensagemErro = validarSenha(senha);
            if (mensagemErro == null) {
                System.out.println("Senha cadastrada com sucesso!!!!!");
                break;
            } else {
                System.out.println("Erro: " + mensagemErro);
            }
        }
        scanner.close();
    }

    public static String validarSenha(String senha) {
        if (senha.length() < 8) {
            return "A senha deve ter no minimo 8 caracteres.";
        }
        if (!Pattern.compile("[A-Z]").matcher(senha).find()) {
            return "A senha deve conter pelo menos uma letra maiuscula.";
        }
        if (!Pattern.compile("[0-9]").matcher(senha).find()) {
            return "A senha deve conter pelo menos um numero.";
        }
        if (!Pattern.compile("[^a-zA-Z0-9]").matcher(senha).find()) {
            return "A senha deve conter pelo menos um caractere especial (@, #, $, etc.).";
        }
        return null;
    }
}
