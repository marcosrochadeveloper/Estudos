<?php
// Configuração do banco de dados
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "refeicoes";

// Conexão com o banco de dados
$conn = new mysqli($servername, $username, $password, $dbname);

// Verifica conexão
if ($conn->connect_error) {
    die("Conexão falhou: " . $conn->connect_error);
}

// Se o formulário for enviado, insere as escolhas no banco de dados
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    foreach ($_POST as $refeicao => $opcao) {
        if (!empty($opcao)) {
            $stmt = $conn->prepare("INSERT INTO escolhas (refeicao, opcao) VALUES (?, ?)");
            $stmt->bind_param("si", $refeicao, $opcao);
            $stmt->execute();
        }
    }
    echo "<p>Escolhas salvas com sucesso!</p>";
}

// Função para gerar tabelas
function gerarTabela($refeicao, $opcoes) {
    echo "<h2>$refeicao</h2>";
    echo "<table border='1'>";
    echo "<tr><th>Opção</th><th>Detalhes</th><th>Selecionar</th></tr>";

    foreach ($opcoes as $num => $detalhes) {
        echo "<tr>";
        echo "<td>Opção $num</td>";
        echo "<td>$detalhes</td>";
        echo "<td><input type='radio' name='$refeicao' value='$num'></td>";
        echo "</tr>";
    }
    echo "</table>";
}

// Definição das opções
$opcoes = [
    "Café da Manhã" => [
        1 => "3 ovos ou 60g de queijo coalho ou 40g de queijo muçarela + 2 fatias de pão de forma",
        2 => "3 ovos ou 60g de queijo coalho ou 40g de muçarela + 100g de cuscuz ou batata-doce + fruta",
        3 => "3 ovos ou 60g de queijo coalho ou 40g de muçarela + 100g de banana + 20g de aveia"
    ],
    "Lanche da Manhã" => [
        1 => "300g de mamão, abacaxi ou maçã, ou 200g de uva",
        2 => "2 fatias de pão de forma",
        3 => "1 copo de iogurte natural integral"
    ],
    "Almoço" => [
        1 => "150g de frango, 100g de patinho ou 150g de peixe + 50g de arroz + 70g de feijão + fruta + salada",
        2 => "150g de frango, 100g de patinho ou 150g de peixe + 150g de macaxeira + fruta + salada",
        3 => "150g de frango, 100g de patinho ou 150g de peixe + 80g de macarrão + fruta + salada"
    ],
    "Lanche da Tarde" => [
        1 => "100g de banana + 20g de aveia",
        2 => "2 fatias de pão de forma + 1 ovo ou 20g de queijo",
        3 => "1 copo de iogurte natural + 10g de chia ou linhaça"
    ],
    "Janta" => [
        1 => "150g de frango, 100g de patinho ou 150g de peixe + 150g de batata-doce ou cuscuz + fruta",
        2 => "150g de frango, 100g de patinho ou 150g de peixe + 100g de macarrão + fruta",
        3 => "150g de frango, 100g de patinho ou 150g de peixe + 100g de macaxeira + fruta"
    ],
    "Ceia" => [
        1 => "100g de frango, patinho ou peixe + 100g de batata-doce ou cuscuz + fruta",
        2 => "100g de frango, patinho ou peixe + 70g de macarrão + fruta",
        3 => "100g de frango, patinho ou peixe + 80g de macaxeira + fruta"
    ]
];

?>

<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Escolha suas Refeições</title>
</head>
<body>

<h1>Escolha suas Refeições</h1>
<form method="post">

    <?php
    foreach ($opcoes as $refeicao => $lista_opcoes) {
        gerarTabela($refeicao, $lista_opcoes);
        echo "<br>";
    }
    ?>

    <button type="submit">Enviar</button>
</form>

</body>
</html>

<?php $conn->close(); ?>