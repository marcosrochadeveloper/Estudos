/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package telas;

import java.awt.Font;

/**
 *
 * @author Marcos
 */
public class TelaGenio extends javax.swing.JFrame {

    /**
     * Creates new form TelaGenio
     */
    public TelaGenio() { //CONSTRUTOR
        initComponents();
        resultadoPalpite.setText("<html>Vou pensar em um número entre <strong>1 e 5</strong>. Tente adivinhar.</html>");
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        resultadoPalpite = new javax.swing.JLabel();
        jLabel1 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        numeroPalpite = new javax.swing.JSpinner();
        btnPalpite = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        resultadoPalpite.setBackground(new java.awt.Color(255, 255, 255));
        resultadoPalpite.setFont(new java.awt.Font("Segoe UI", 0, 14)); // NOI18N
        resultadoPalpite.setForeground(new java.awt.Color(0, 0, 0));
        resultadoPalpite.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        resultadoPalpite.setText("Frase");
        resultadoPalpite.setVerticalAlignment(javax.swing.SwingConstants.TOP);
        getContentPane().add(resultadoPalpite, new org.netbeans.lib.awtextra.AbsoluteConstraints(60, 50, 140, 80));

        jLabel1.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagens/genio.png"))); // NOI18N
        getContentPane().add(jLabel1, new org.netbeans.lib.awtextra.AbsoluteConstraints(210, 100, -1, 213));

        jLabel3.setText("Valor");
        getContentPane().add(jLabel3, new org.netbeans.lib.awtextra.AbsoluteConstraints(60, 210, 37, -1));

        jLabel2.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagens/balao.png"))); // NOI18N
        getContentPane().add(jLabel2, new org.netbeans.lib.awtextra.AbsoluteConstraints(30, 20, 210, -1));

        numeroPalpite.setModel(new javax.swing.SpinnerNumberModel(0, 0, 5, 1));
        getContentPane().add(numeroPalpite, new org.netbeans.lib.awtextra.AbsoluteConstraints(100, 210, -1, -1));

        btnPalpite.setText("Palpite");
        btnPalpite.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnPalpiteActionPerformed(evt);
            }
        });
        getContentPane().add(btnPalpite, new org.netbeans.lib.awtextra.AbsoluteConstraints(70, 250, -1, -1));

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnPalpiteActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnPalpiteActionPerformed
        double ale = Math.random();
        int numero = (int) (1 + ale * (6-1));
        
        int palpite = (int) numeroPalpite.getValue();
        String resultado = (numero == palpite) ? "<html><strong>ACERTOU!</strong></html>":"<html>ERROU! Eu pensei no número <strong>" + numero + "</strong></html>";
        
        resultadoPalpite.setFont(new Font("Arial Black", Font.PLAIN, 16));
        resultadoPalpite.setText(resultado);
    }//GEN-LAST:event_btnPalpiteActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(TelaGenio.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(TelaGenio.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(TelaGenio.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(TelaGenio.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new TelaGenio().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnPalpite;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JSpinner numeroPalpite;
    private javax.swing.JLabel resultadoPalpite;
    // End of variables declaration//GEN-END:variables
}
