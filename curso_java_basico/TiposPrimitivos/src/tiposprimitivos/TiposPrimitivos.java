package tiposprimitivos;

import java.util.Scanner;

public class TiposPrimitivos {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        
        System.out.print("Digite seu nome: ");
        String nome = teclado.nextLine();
        
        System.out.printf("Olá %s, informe sua nota: ", nome);
        float nota = teclado.nextFloat();
        
//        System.out.println("Sua nota é " + nota);
//        System.out.printf("%s, sua nota é %.1f \n", nome, nota);
        System.out.println("--- RESPOSTA ---");
        System.out.format("%s, sua nota é %.1f \n", nome, nota);
    }
    
}
