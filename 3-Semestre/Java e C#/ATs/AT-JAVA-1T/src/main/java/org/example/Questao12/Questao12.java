package org.example.Questao12;
import java.util.Scanner;

public class Questao12 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] mensagens = new String[10];
        int contadorMensagens = 0;

        System.out.print("Digite o nome do primeiro usuario: ");
        String usuario1 = scanner.nextLine();
        System.out.print("Digite o nome do segundo usuario: ");
        String usuario2 = scanner.nextLine();

        while (contadorMensagens < 10) {
            if (contadorMensagens % 2 == 0) {
                System.out.print(usuario1 + ", digite sua mensagem: ");
                mensagens[contadorMensagens] = usuario1 + ": " + scanner.nextLine();
            } else {
                System.out.print(usuario2 + ", digite sua mensagem: ");
                mensagens[contadorMensagens] = usuario2 + ": " + scanner.nextLine();
            }
            contadorMensagens++ ;
        }
        System.out.println("\nHistorico das mensagens");
        for (String mensagem : mensagens) { System.out.println(mensagem); }
        scanner.close();
    }
}
