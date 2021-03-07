<html>
  <head>
        <title>Reservar</title>
        <meta charset="utf-8"/> 
        <link rel="stylesheet" type="text/css" href="estilo.css">
  </head>
    
<body> 
<?php

$txNome = $_GET['txNome'];
$txApt = $_GET['txApt'];
$Dia = $_GET['Dia'];
$Horario = $_GET['Horario'];

date_default_timezone_set('America/Fortaleza');
function dateDiff( $col3, $horaAcesso, $format = '%a' ) {

    $d1     =   new DateTime( $col3 );
  
    $d2     =   new DateTime( $horaAcesso );
  
    //Calcula a diferença entre as datas
    $diff   =   $d1->diff($d2, true);   
  
    //Formata no padrão esperado e retorna
    return $diff->format( '%H' );
  
  }





$mysqli = new mysqli("sql311.epizy.com", "epiz_26899380", "ZEWjmtPlObYRX9r", "epiz_26899380_reserva");

if (mysqli_connect_errno()) {
    printf("Connect failed: %s\n", mysqli_connect_error());
    exit();
}


$horaAcesso = date('H:i:s');
if ($txApt){
    if ($stmt = $mysqli->prepare("INSERT INTO reserva (nome, apt, dia, horario, horarioAcesso) VALUES ('$txNome' , '$txApt','$Dia' , '$Horario', '$horaAcesso')")) {
        $result = $stmt->execute();
    
        if ($result) {
         } else {
            echo "<div id= 'container'> <h1> <br>Não foi possivel agendar sua reserva! </h1> <h3> Horário já reservado. </h3>    ";
            echo "<button onclick=\"window.location.href ='consultar.php'\" class=\"submit\">Consultar</button></div>";
            exit;
         }
        
         $stmt->close();
        
    }
    }


if ($stmt = $mysqli->prepare("SELECT dia, horario, horarioAcesso, autorizacao FROM reserva")) {
    $stmt->execute();
  
    /* bind variables to prepared statement */
    $stmt->bind_result($col1, $col2, $col3, $col4);
    
  
    /* fetch values */
    while ($stmt->fetch()) {
        $diferenca = dateDiff($col3, $horaAcesso);
        
  
        if ($diferenca >=1 and$col4 == 0 ) {            
            header("Location: deletar.php?dia='$col1'&horario='$col2'&autorizacao='$col4'&diferenca='$diferenca'");            
        }    
  
  
    } 
    echo "<div id= 'container'> <h1> <br>Sua reserva foi realizada com sucesso! </h1> <h3> Confirme sua reserva em até uma hora,<br> ou ela será cancelada! </h3>  ";
    echo "<button onclick=\"window.location.href ='consultar.php'\" class=\"submit\">Consultar</button></div>";      
    
  }

$mysqli->close();



?>
</body>
</html>