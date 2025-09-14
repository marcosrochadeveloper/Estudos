package operadoresaritmeticos;

import java.util.Scanner;

public class OperadoresAritmeticos {

    public static void main(String[] args) {
//        Scanner teclado = new Scanner(System.in);
//        System.out.print("Informe o Primeiro Número: ");
//        int n1 = teclado.nextInt();
//        System.out.print("Informe o Segundo Número: ");
//        int n2 = teclado.nextInt();
//        int adicao = n1 + n2;
//        int subtracao = n1 - n2;
//        int multiplicacao = n1 * n2;
//        float divisao = n1 / n2;
//        int resto = n1 % n2;
//        float media = (n1 + n2) / 2;
//        
//        System.out.printf("%d mais %d é igual a %d \n", n1, n2, adicao);
//        System.out.printf("%d menos %d é igual a %d \n", n1, n2, subtracao);
//        System.out.printf("%d vezes %d é igual a %d \n", n1, n2, multiplicacao);
//        System.out.printf("%d dividido por %d é igual a %.2f \n", n1, n2, divisao);
//        System.out.printf("O resto da divisão de %d por %d é igual a %d \n", n1, n2, resto);
//        System.out.println("A média é igual a " + media);
//        
//        int numero = 10;
//        int valor = 4 + numero--;
//        System.out.println(valor);
//        System.out.println(numero);
//
//        int x = 4;
//        x *= 2; // x = x * 2;
//        System.out.println(x);

//        float v = 8.3f;
//        int arBaixo = (int) Math.floor(v);
//        int arCima = (int) Math.ceil(v);
//        int arAutomatico = (int) Math.round(v);
//        System.out.println("------ O NÚMERO " + v + " ------");
//        System.out.println("Arredondando para baixo, ficaria " + arBaixo);
//        System.out.println("Arredondando para cima, ficaria " + arCima);
//        System.out.println("Arredondando Aritmeticamente, ficaria " + arAutomatico);

        double ale = Math.random();
        int numero = (int) (0 + ale * (11-0));
        System.out.println(ale);
        System.out.println(numero);
    }
    
}