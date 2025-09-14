package idiomasistema;

import java.util.Locale;

public class IdiomaSistema {

    public static void main(String[] args) {
        Locale idioma = Locale.getDefault();
        String nomeIdioma = idioma.getDisplayName();
        System.out.println("Seu sistema está em " + nomeIdioma);
    }
    
}
