package programavoto;

import java.util.Scanner;

public class ProgramaVoto {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Qual o seu ano de nascimento? ");
        int nascimento = input.nextInt();
        int idade = 2025 - nascimento;
        String situacao;
        System.out.println("Você tem " + idade + " anos.");
        
        if (idade < 16 ){
            situacao = "Você não vota ainda!";
        } else {
            if ((idade < 18) || (idade > 70)) {
                situacao = "Seu voto é Opcional";
            } else{
                situacao = "Seu voto é Obrigatório!";
            }
        }
        
        System.out.println(situacao);
    }
    
}
