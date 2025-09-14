
package programamedia;

import java.util.Scanner;

public class ProgramaMedia {

    public static void main(String[] args) {
        float n1, n2, m;
        Scanner input = new Scanner(System.in);
        
        System.out.print("Primeira Nota: ");
        n1 = input.nextFloat();
        
        System.out.print("Segunda Nota: ");
        n2 = input.nextFloat();
        
        m = (n1 + n2) / 2;
        
        System.out.println("Sua média foi " + m);
        
        if (m >= 9){
            System.out.println("Parabéns, pequeno gafanhoto!");
        }
    }
    
}
