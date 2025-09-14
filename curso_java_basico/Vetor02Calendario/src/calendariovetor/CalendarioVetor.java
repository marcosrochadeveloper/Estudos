package calendariovetor;

import java.util.Scanner;

public class CalendarioVetor {

    public static void main(String[] args) {
        String mes[] = {"Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"};
        int tot[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        
        Scanner input = new Scanner(System.in);
        
        System.out.print("Informe um ano: ");
        int ano = input.nextInt();
        
        boolean bissexto = (ano % 4 == 0 && (ano % 100 != 0 || ano % 400 == 0));
        
//        if (ano % 4 == 0){
//            if (ano%100 == 0){
//                if (ano%400 == 0){
//                    bissexto = true;
//                } else {
//                    bissexto = false;
//                }
//            } else{
//                bissexto = true;
//            }
//        } else{
//            bissexto = false;
//        }
        
        if (bissexto){
            System.out.println("O ano " + ano + " é bissexto");
            tot[1] = 29;
        } else{
            System.out.println("O ano " + ano + " não é bissexto");
        }
        
        for (int c = 0; c < mes.length; c++){
            System.out.println("O mês de " + mes[c] + " tem " + tot[c] + " dias ao todo.");
        }
    }
}
