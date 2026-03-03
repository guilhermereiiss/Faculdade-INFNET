package org.example.TP2;

import java.util.Scanner;

public class Questao9 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Cadastre sua senha: ");
        String senhaCadastro = scanner.nextLine();

        String senhaDigitada;
        do {
            System.out.print("Digite novamente a senha: ");
            senhaDigitada = scanner.nextLine();

            if (!senhaCadastro.equals(senhaDigitada)) {
                System.out.println("Senha incorreta. Tente novamente.");
            }

        } while (!senhaCadastro.equals(senhaDigitada));

        System.out.println("Senha cadastrada com sucesso!");

        scanner.close();
    }
}
