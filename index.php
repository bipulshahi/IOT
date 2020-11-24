

<html>  
  <head>      
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Bulb for ESP8266</title>

    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
  </head>
  <body>
    <h2 align="center">Internet of Things</h2>
    <div class="row" style="margin-top: 20px;">
      <div class="col-md-8 col-md-offset-2">
        <a id="light_on" href="?light=on" class="btn btn-success btn-block btn-lg">Turn On</a>
        <br />
        <a id="light_off" href="?light=off" class="led btn btn-danger btn-block btn-lg">Turn Off</a>
        <br />
      </div>
    </div>
  </body>
</html>  

<?php
 
  if ($_GET['light']){

    $servername = "localhost";
    $username = "umang";
    $password = "umang@!1122";
    $dbname = "iot";

    // Create connection
    $conn = mysqli_connect($servername, $username, $password, $dbname);
		
    $light = $_GET['light'];
	
	if($light == "on"){
		$light = '1';
	}
	else if($light == "off"){
		$light = '0';
	}
		
	$sql = "update home set value = '$light'";
		
     if(mysqli_query($conn,$sql)){
		 
		 if($light == "1"){
			echo "<center><img src='images/on.png' width='200'></img></center>";
		}
		else if($light == "0"){
			echo "<center><img src='images/off.png' width='250'></img></center>";
		}
		 
	 }
	 else{
		 echo "<center><p>Failed</p></center>";
	 }
	 
	$conn->close();
  }

?>