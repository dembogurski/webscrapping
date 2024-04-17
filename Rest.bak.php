<?php

/**
 * @author Doglas A. Dembogurski
 */
class Rest {

 function __construct() {
        $action = $_REQUEST['action'];
        if (isset($action)) {
            $this->{$action}();
        } else {
            $this->main();
        }
    }
    function main() {
        echo "Main...";
    }
    function generarPresupuestos(){
        $urls = json_decode( $_REQUEST['urls'] );
        $porc_recargo =  $_REQUEST['porc_recargo'] ;
        $pagina =  $_REQUEST['pagina'] ;
        
        echo $porc_recargo ."<br>".$pagina."<br><br>";
        
        for ($i = 0; $i < count($urls); $i++){
            //echo "$i >>> ". $urls[$i]."<br>";
            
            $url = $urls[$i];
            
            //$command = escapeshellcmd("python $pagina.py " . escapeshellarg($url) . " " . escapeshellarg($aumento)." $i");

            $command = "python  $pagina.py   $url   $porc_recargo  $i";
            
            echo $command."<br>";
            
            $output = shell_exec($command);
            
            
            echo "Salida $output<br>";
        }
    } 
}
 
new Rest();

?>

