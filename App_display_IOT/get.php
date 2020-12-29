<?php

$host = "localhost";
$user = "id14277162_umang";
$pass = "A5D+3-WH|vm}fC77";
$db = "id14277162_myblog";

$connection = mysqli_connect($host,$user,$pass,$db);

$sql = "select * from data";

$res = mysqli_query($connection,$sql);  ###execute the query

$result = array();   ##declared a blank array

while($row=mysqli_fetch_array($res)){
	array_push($result,array('temp'=>$row['temp'],
							'humidity'=>$row['humidity']));
}

echo json_encode(array('sensor'=>$result));

mysqli_close($connection);

?>