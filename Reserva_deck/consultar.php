<!-- **** Consulta SQL com comandos preparados **** -->

<html>
  <head>
        <title>CONSULTA BD</title>
        <meta charset="utf-8"/> 
        <style>
        table {
          margin: auto;
  color: #ff0000;
  font-weight: bold;
	font-family: arial, sans-serif;
	border-collapse: collapse;
	width: 70%;
	}

td, th {
  margin: auto;
	border: 1px solid #ffffff;
	text-align: center;
	padding: 3px;
	}

tr:nth-child(even) {
  margin: auto;
	background-color: #22190ce5;
	}
        </style>
         <link rel="stylesheet" type="text/css" href="estilo.css">
  </head>
    
<body> 
<?php
date_default_timezone_set('America/Fortaleza');

    
//Config. para acesso ao mySql localmente 
$servername = "sql311.epizy.com";
$username = "epiz_26899380";
$password = "ZEWjmtPlObYRX9r";
$dbname = "epiz_26899380_reserva";

$conn = mysqli_connect($servername, $username, $password);


if (!$conn) 
{
  die("Falha na Conexão: " . mysqli_connect_error());
}



// Selecionando banco
if (!mysqli_select_db($conn, $dbname)) 
{
    echo "Não foi possível selecionar base de dados \"$dbname\": " . mysqli_error($conn);
    exit;
}

date_default_timezone_set('America/Fortaleza');



$sql = "SELECT nome, apt, dia, horario, autorizacao, horarioAcesso FROM reserva";

//stmt = statment ou comando
//stmt é o comando a ser preparado    
$stmt = mysqli_stmt_init($conn);    
$stmt_prepared_okay = mysqli_stmt_prepare($stmt, $sql);  
  
/* create a prepared statement */
if ($stmt_prepared_okay) 
{
    /* Liga parametros com os marcadores */
    //mysqli_stmt_bind_param($stmt, "i", $numc);

    /* executa a query */
    mysqli_stmt_execute($stmt);

    /* liga as variávais de resultado */
    mysqli_stmt_bind_result($stmt, $nome, $apt, $dia, $horario, $autorizacao, $horario_de_acesso);

    /* busca os valores */
    echo "<br><br><h1>RESERVAS DA SEMANA</h1>";
    while(mysqli_stmt_fetch($stmt))
    {
          echo "<table>
    <tr>
      <th>Nome</th>
      <th>Apartamento</th>
      <th>Dia</th>
      <th>Horário</th>
      <th>Horário de Acesso</th>
      <th>Confirmar</th>
    </tr>
    <tr>
      <td> $nome</td>
      <td> $apt</td>
      <td> $dia</td>
      <td> $horario</td>
      <td> $horario_de_acesso</td>
      <td>";
      if($autorizacao == 0){
        echo "<button onclick=\"window.location.href ='confirmar.php?dia=$dia&horario=$horario'\">Confirmar</button>";
      }else{
        echo"CONFIRMADO";
        
      }
      
      echo"</td>
    </tr>
  </table>";
    }
    mysqli_stmt_close($stmt);
    /* close statement */
    
}    




?>

  

</body>
<br>
<button onclick="window.location.href ='index.html'" class="submit" text-align:left>Página Inicial!</button><br>
</html>