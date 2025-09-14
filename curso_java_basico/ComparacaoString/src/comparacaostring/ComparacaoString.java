package comparacaostring;

public class ComparacaoString {

    public static void main(String[] args) {
        String nome1 = "Marcos";
        String nome2 = "Marcos";
        String nome3 = new String("Marcos");
        String res;
        res = (nome1 == nome3)?"igual":"diferente";
        System.out.println(res);
        res = (nome1.equals(nome3))?"igual":"diferente";
        System.out.println(res);
    }
    
}
