<?php
$servername = "mysql.zzz.com.ua";
$username = "rspwncomp";
$password = "1337rspwncomP";
$dbname = "treamz";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$uname = isset($_POST['username']) ? $_POST['username'] : '';

$sql = "SELECT username, refs FROM rspwn_comp1 WHERE username='$uname' LIMIT 1";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "username: " . $row["username"]. " - refs: " . $row["ref"]. "<br>";
    }
} else {
    echo "0 results";
    $uname = isset($_POST['username']) ? $_POST['username'] : '';
    $sql = "INSERT INTO rspwn_comp1 (username, refs)
 	VALUES ('$uname', '0')";

	if ($conn->query($sql) === TRUE) {
    		echo "New record created successfully";
	} else {
    		echo "Error: " . $sql . "<br>" . $conn->error;
	}
}
$conn->close();
?>