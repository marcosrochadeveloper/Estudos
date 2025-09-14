package programaidade;

import java.util.Scanner;

public class ProgramaIdade {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int nascimento, idade;
        
        System.out.print("Em que ano você nasceu? ");
        nascimento = input.nextInt();
        
        idade = 2025 - nascimento;
        
        System.out.println("Você tem " + idade + " anos");
        if (idade >= 18){
            System.out.println("Maior de Idade");
        } else{
            System.out.println("Menor de Idade");
        }
    }
}
