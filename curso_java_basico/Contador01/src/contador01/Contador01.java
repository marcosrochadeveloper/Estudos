package contador01;

import java.util.Scanner;

public class Contador01 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int cc = 0;
        
        System.out.print("Quantas Cambalhotas? ");
        int cambalhotas = input.nextInt();
        
        while (cc < cambalhotas){
            cc++;
            
            if(cc == 2 || cc == 3 || cc == 4){
                continue;
            }
            
            if (cc == 7){
                break;
            }
            
            System.out.println("Cambalhota " + cc);
        }
    }
    
}
