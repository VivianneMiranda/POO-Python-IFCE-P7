<?php
date_default_timezone_set('America/Fortaleza');

$dia = $_GET['dia'];
$horario = $_GET['horario'];


$conn = mysql_connect("sql311.epizy.com", "epiz_26899380", "ZEWjmtPlObYRX9r");
if (!$conn) {
    echo "Nao foi possivel conectar ao banco de dados: " . mysql_error();
    exit;
}
mysql_set_charset('UTF-8');

// Selecionando banco
if (!mysql_select_db("epiz_26899380_reserva")) {
    echo "Nao foi possivel selecionar tabela: " . mysql_error();
    exit;
}


$sql = "DELETE FROM reserva WHERE dia = ". $dia . " and horario =". $horario ."";
$result = mysql_query($sql);

mysql_free_result($result);

header('Location: inserirNET.php');

?>
