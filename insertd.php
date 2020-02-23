<?php
//create new record as per request
//connection with database

	$servername = "localhost";
	$username = "id12681516_bdtaskdata";
	$password = "abcde123";
	$dbname = "id12681516_bdtask";
	
	$conn = mysqli_connect($servername,$username,$password,$dbname);

	date_default_timezone_set('Asia/Dhaka');
	$d = date("Y-m-d");
	$t = date("H:i:s");
	
	$hum = $_GET['h'];
	$temp = $_GET['t'];
	
	$sql = "INSERT INTO sensor_values (humidity,temperature,date,time) VALUES ('$hum','$temp','$d','$t')";
	if(mysqli_query($conn,$sql)){
		echo "Connection and upload succeed";
	}
	else{
		echo mysqli_error($conn);
	}
	$conn->close();
?>