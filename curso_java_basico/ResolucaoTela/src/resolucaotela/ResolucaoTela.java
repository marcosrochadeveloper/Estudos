package resolucaotela;

import java.awt.Dimension;
import java.awt.Toolkit;

public class ResolucaoTela {

    public static void main(String[] args) {
        Toolkit toolkit = Toolkit.getDefaultToolkit();
        
        Dimension screenSize = toolkit.getScreenSize();
        
        int largura = screenSize.width;
        int altura = screenSize.height;
        
        System.out.println("Sua tela tem resolução " + largura + " x " + altura);
    }
    
}
