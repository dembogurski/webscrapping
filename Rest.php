<?php

class Rest {

    function __construct() {
        $action = $_REQUEST['action'] ; // Default to main if 'action' is not set
        if (method_exists($this, $action)) {
            $this->{$action}();
        } else {
            $this->main();
        }
    }

    function main() {
        echo "Main...";
    }

    function generarPresupuestos(){
        $urls = json_decode($_REQUEST['urls'], true);
        $porc_recargo = $_REQUEST['porc_recargo'];
        $pagina = $_REQUEST['pagina'];
        
        //echo $porc_recargo ."<br>".$pagina."<br><br>";
        
        foreach ($urls as $i => $url) {
            $command = "C:\\Python310\\python.exe " . escapeshellcmd($pagina . ".py") . " " . escapeshellarg($url) . " " . escapeshellarg($porc_recargo) . " " . escapeshellarg($i) . " 2>&1";
            //echo $command . "<br>";
            $output = shell_exec($command);
            //echo "Salida: $output<br>";
        }
        
        echo json_encode(array("mensaje"=>"Ok"));
    }
}

new Rest();

?>
