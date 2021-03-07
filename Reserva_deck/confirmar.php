<?php
$Dia = $_GET['dia'];
$Horario = $_GET['horario'];
date_default_timezone_set('America/Fortaleza');



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


$sql = "UPDATE reserva SET autorizacao = 1 where dia= '$Dia' and horario = $Horario";
$result = mysql_query($sql);
header('Location: consultar.php');

mysql_free_result($result);

?>
