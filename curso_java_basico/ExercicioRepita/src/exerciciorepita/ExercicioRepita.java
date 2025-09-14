
package exerciciorepita;

import javax.swing.JOptionPane;

public class ExercicioRepita {

    public static void main(String[] args) {
        int num, soma = 0, totalDeValores = 0, totalDePares = 0, totalDeImpares = 0, acimaDe100 = 0, media;
        do {
            num = Integer.parseInt(JOptionPane.showInputDialog(null,
                    "<html>Informe um valor: <br><em>(Valor 0 interrompe)</em></html>"));
            soma += num;
            if (num != 0){
                totalDeValores++;
                if (num%2 == 0){
                    totalDePares++;
                } else{
                    totalDeImpares++;
                }
                if (num > 100){
                    acimaDe100++;
                }
            };

        } while(num != 0);
        
        media = soma / totalDeValores;
        
        JOptionPane.showMessageDialog(null, "<html> Resultado final"
                + "<hr>" + 
                "<br> Total de Valores: " + totalDeValores + 
                "<br> Total de Pares: " + totalDePares +
                "<br> Total de Ímpares: " + totalDeImpares +
                "<br> Acima de 100: " + acimaDe100 +
                "<br> Média dos valores: " + media +
                "</html>");
    }
    
}

// 4 + 1 + 2 + 7 + 8 + 3 + 6 + 5 + 200 + 150 + 120 + 5 + 9 + 0