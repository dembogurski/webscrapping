<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="iso-8859-1">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Qubit Generador de Presupuestos</title>
    <script src="../../js/jquery-3.3.1.min.js" type="text/javascript"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
            width: 900px;
            margin-top: -300px;
        }
        .form-control {
            margin-bottom: 10px;
        }
        .buttons {
            display: flex;
            justify-content: space-around;
        }
        button {
            padding: 10px 20px;
            cursor: pointer;
        }
        textarea {
            width: 100%;
            height: 100px;
        }
        .div_flex{
            display: flex;
            justify-content: center
        }
    </style>
     
</head>
<body>
    <div class="container">
        <h2>Qubit E.A.S. Generador de Presupuestos</h2>
        <form>
            <div class="form-control div_flex">
                <input type="radio" name="option" value="VisaoVip" id="VisaoVip" checked="checked"><label for="VisaoVip">VisaoVip</label>
                <input type="radio" name="option" value="Nissei" id="Nissei"><label  for="Nissei">Nissei</label> 
                <input type="radio" name="option" value="CellShop" id="CellShop"><label  for="CellShop">CellShop</label>
            </div>
            <div class="form-control div_flex">
                <label for="urls"><strong>URLs:</strong></label><br>
                <textarea id="urls" name="urls" ></textarea>
            </div>
            <div class="buttons">
                <button type="button" onclick="cancelar()">Cancelar</button> 
                <div><label>% Recargo</label> <input type="text" id="porc_recargo" value="25" style="width: 40px;text-align: center"></div>
                <button type="button" onclick="generarPresupuestos()">Generar Presupuestos</button>
            </div>
            
            <div>
                <div id="msg"></div>
               <button type="button" onclick="abrirCarpeta()">Abrir Presupuestos</button>
            </div>    
        </form>
    </div>
    
    <script>
        function cancelar() {            
            document.querySelector('form').reset();
        }
        
        function generarPresupuestos(){
            var urls = $("#urls").val().split("\n");
            var pagina = $("input[name=option]:checked").val();
            var porc_recargo = $("#porc_recargo").val();
            urls = JSON.stringify(urls);
            
            console.log(urls);
            
            $.ajax({
                type: "POST",
                url: "Rest.php",
                data: {action:"generarPresupuestos", urls: urls,pagina:pagina,porc_recargo:porc_recargo },
                async: true,
                dataType: "json",
                beforeSend: function() {
                    $("#msg").html("<img src='../../img/loading_fast.gif' width='16px' height='16px' >"); 
                },
                success: function(data) {   
                    $("#msg").html("Listo puede abrir los presupuestos..."); 
                }
            });
        } 
        
        function abrirCarpeta(){
            window.open("http://localhost/qubit/utils/webscrapping/files/");
        }
        
    </script>
</body>
</html>
