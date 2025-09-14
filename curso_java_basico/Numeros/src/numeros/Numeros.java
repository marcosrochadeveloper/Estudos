package numeros;

import java.util.Scanner;

public class Numeros {

    public static void main(String[] args) {
        int num, soma=0;
        String resposta;
        Scanner input = new Scanner(System.in);
        do {
            System.out.print("Digite um número: ");
            num = input.nextInt();
            soma += num; // soma = soma + num;
            System.out.print("Quer continuar? [S/N] ");
            resposta = input.next();
        } while(resposta.equals("S"));
        System.out.println("A soma de todos os valores é " + soma);
        
    }
    
}
