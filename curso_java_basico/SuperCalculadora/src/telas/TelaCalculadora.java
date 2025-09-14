package telas;

public class TelaCalculadora extends javax.swing.JFrame {

    public TelaCalculadora() { //CONSTRUTOR
        initComponents();
        painelCalculos.setVisible(false);
        
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jLabel1 = new javax.swing.JLabel();
        txtValor = new javax.swing.JSpinner();
        btnCalcular = new javax.swing.JButton();
        jLabel3 = new javax.swing.JLabel();
        jLabel13 = new javax.swing.JLabel();
        painelCalculos = new javax.swing.JPanel();
        raizCubica = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        raizQuadrada = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        elevadoAoCubo = new javax.swing.JLabel();
        restoDivisao = new javax.swing.JLabel();
        valorAbsoluto = new javax.swing.JLabel();
        jLabel6 = new javax.swing.JLabel();
        jLabel7 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setPreferredSize(new java.awt.Dimension(504, 450));
        setResizable(false);

        jLabel1.setFont(new java.awt.Font("Lucida Sans Typewriter", 1, 24)); // NOI18N
        jLabel1.setText("Super Calculadora");

        txtValor.setModel(new javax.swing.SpinnerNumberModel());

        btnCalcular.setFont(new java.awt.Font("Segoe UI", 0, 18)); // NOI18N
        btnCalcular.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagens/operadores.png"))); // NOI18N
        btnCalcular.setText("Calcular");
        btnCalcular.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        btnCalcular.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnCalcularActionPerformed(evt);
            }
        });

        jLabel3.setText("Informe um valor:");

        jLabel13.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagens/calculator-icon.png"))); // NOI18N

        raizCubica.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        raizCubica.setForeground(new java.awt.Color(0, 153, 255));
        raizCubica.setText("0");

        jLabel5.setText("Raiz Quadrada");

        raizQuadrada.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        raizQuadrada.setForeground(new java.awt.Color(0, 153, 255));
        raizQuadrada.setText("0");

        jLabel4.setText("Elevado ao Cubo");

        elevadoAoCubo.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        elevadoAoCubo.setForeground(new java.awt.Color(0, 153, 255));
        elevadoAoCubo.setText("0");

        restoDivisao.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        restoDivisao.setForeground(new java.awt.Color(0, 153, 255));
        restoDivisao.setText("0");

        valorAbsoluto.setFont(new java.awt.Font("Segoe UI", 1, 18)); // NOI18N
        valorAbsoluto.setForeground(new java.awt.Color(0, 153, 255));
        valorAbsoluto.setText("0");

        jLabel6.setText("Raiz Cúbica");

        jLabel7.setText("Valor Absoluto");

        jLabel2.setText("Resto da Divisão por 2");

        javax.swing.GroupLayout painelCalculosLayout = new javax.swing.GroupLayout(painelCalculos);
        painelCalculos.setLayout(painelCalculosLayout);
        painelCalculosLayout.setHorizontalGroup(
            painelCalculosLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(painelCalculosLayout.createSequentialGroup()
                .addGap(26, 26, 26)
                .addGroup(painelCalculosLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jLabel5, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 132, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel6, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 132, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel7, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 132, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addGroup(painelCalculosLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                        .addComponent(jLabel2, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 132, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addComponent(jLabel4, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 132, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 29, Short.MAX_VALUE)
                .addGroup(painelCalculosLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(valorAbsoluto, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 90, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(raizCubica, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 90, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(raizQuadrada, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 90, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(elevadoAoCubo, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 90, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(restoDivisao, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 90, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap())
        );
        painelCalculosLayout.setVerticalGroup(
            painelCalculosLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, painelCalculosLayout.createSequentialGroup()
                .addContainerGap()
                .addGroup(painelCalculosLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel2)
                    .addComponent(restoDivisao))
                .addGap(18, 18, 18)
                .addGroup(painelCalculosLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel4)
                    .addComponent(elevadoAoCubo))
                .addGap(17, 17, 17)
                .addGroup(painelCalculosLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel5)
                    .addComponent(raizQuadrada))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 20, Short.MAX_VALUE)
                .addGroup(painelCalculosLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel6)
                    .addComponent(raizCubica))
                .addGap(17, 17, 17)
                .addGroup(painelCalculosLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel7)
                    .addComponent(valorAbsoluto))
                .addGap(15, 15, 15))
        );

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING, false)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(46, 46, 46)
                        .addComponent(jLabel3, javax.swing.GroupLayout.PREFERRED_SIZE, 106, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(txtValor, javax.swing.GroupLayout.PREFERRED_SIZE, 78, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(btnCalcular))
                    .addGroup(javax.swing.GroupLayout.Alignment.LEADING, layout.createSequentialGroup()
                        .addGap(160, 160, 160)
                        .addComponent(jLabel1, javax.swing.GroupLayout.PREFERRED_SIZE, 257, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addContainerGap(54, Short.MAX_VALUE))
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(painelCalculos, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(jLabel13, javax.swing.GroupLayout.PREFERRED_SIZE, 158, javax.swing.GroupLayout.PREFERRED_SIZE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(15, 15, 15)
                .addComponent(jLabel1)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(27, 27, 27)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(jLabel3)
                            .addComponent(txtValor, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)))
                    .addComponent(btnCalcular))
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(painelCalculos, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addContainerGap(18, Short.MAX_VALUE))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(jLabel13, javax.swing.GroupLayout.PREFERRED_SIZE, 213, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addContainerGap())))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void btnCalcularActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnCalcularActionPerformed
        // TODO add your handling code here:
        int valor = (int) txtValor.getValue();
        
        // RESTO DA DIVISÃO POR 2
        int resto = valor % 2;
        restoDivisao.setText(Integer.toString(resto));
        
        // ELEVADO AO CUBO
        double elevado = Math.pow(valor, 3);
        elevadoAoCubo.setText(String.format("%.2f", elevado));
        
        // RAIZ QUADRADA
        double raizQ = (double) Math.sqrt(valor);
        raizQuadrada.setText(String.format("%.2f", raizQ));
        
        // RAIZ CUBICA
        double raizC = (double) Math.cbrt(valor);
        raizCubica.setText(String.format("%.2f", raizC));
        
        // VALOR ABSOLUTO
        int absoluto = (int) Math.abs(valor);
        valorAbsoluto.setText(Integer.toString(absoluto));

        // TORNAR O PAINEL VISÍVEL
        painelCalculos.setVisible(true);
    }//GEN-LAST:event_btnCalcularActionPerformed

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
            java.util.logging.Logger.getLogger(TelaCalculadora.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(TelaCalculadora.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(TelaCalculadora.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(TelaCalculadora.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new TelaCalculadora().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton btnCalcular;
    private javax.swing.JLabel elevadoAoCubo;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel13;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JPanel painelCalculos;
    private javax.swing.JLabel raizCubica;
    private javax.swing.JLabel raizQuadrada;
    private javax.swing.JLabel restoDivisao;
    private javax.swing.JSpinner txtValor;
    private javax.swing.JLabel valorAbsoluto;
    // End of variables declaration//GEN-END:variables
}
