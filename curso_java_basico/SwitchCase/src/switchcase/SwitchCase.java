package switchcase;

import java.util.Scanner;

public class SwitchCase {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String tipo;
        
        System.out.print("Quantas pernas? ");
        int pernas = input.nextInt();
        System.out.print("Isso é um(a) ");
        
        switch (pernas){
            case 1:
                tipo = "Saci";
                break;
            case 2:
                tipo = "Bípede";
                break;
            case 4:
                tipo = "Quadrúpede";
                break;
            case 6,8:
                tipo = "Aranha";
                break;
            default:
                tipo = "ET";
        }
        System.out.println(tipo);
    }
    
}
