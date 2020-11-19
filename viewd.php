<?php

$servername = "localhost";
	$username = "id12681516_bdtaskdata";
	$password = "abcde123";
	$dbname = "id12681516_bdtask";
	
	$conn = mysqli_connect($servername,$username,$password,$dbname);

	if ($conn->connect_error) {
        die("Database Connection failed: " . $conn->connect_error);
        echo "<a href='install.php'>If first time running click here to install database</a>";
    }
$sql = "SELECT * FROM sensor_values ORDER BY id DESC";
if($result = mysqli_query($conn,$sql)){
	//fetch one and one row
	echo "<TABLE>";
	echo "<TR><TH>Sr.No.</TH><TH>HUM</TH><TH>TEMP</TH><TH>Date</TH><TH>Time</TH></TR>";
	while ($row=mysqli_fetch_row($result))
      {
        echo "<TR>";
        echo "<TD>".$row[0]."</TD>";
        echo "<TD>".$row[1]."</TD>";
		echo "<TD>".$row[2]."</TD>";
		echo "<TD>".$row[3]."</TD>";
		echo "<TD>".$row[4]."</TD>";
        echo "</TR>";
      }
	echo"</TABLE>";
	//free result set
	mysqli_free_result($result);
}
mysqli_close($conn);
?>