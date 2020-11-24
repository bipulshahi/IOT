<?php
//Creates new record as per request
    //Connect to database
    $servername = "localhost";
    $username = "umang";
    $password = "umang@!!@@";
    $dbname = "iot";

    // Create connection
    $conn = mysqli_connect($servername, $username, $password, $dbname);
		
	    $sql = "select value from home";
		
		$result = mysqli_query($conn,$sql);
		
		$row = mysqli_fetch_array($result);
		
		$value = $row['value'];
		
		if($value == '0'){
			
		echo "OFF";
		
		}
		
		else if($value == '1'){
			
		echo "ON";
		
		}
		
	 
	$conn->close();
?>