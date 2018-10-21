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
            $sql = "SELECT username,refs
FROM rspwn_comp1
ORDER BY refs DESC
LIMIT 5";
            $result = $conn->query($sql);
            $cart = array();
            if ($result->num_rows > 0) {
                while($row = $result->fetch_assoc()) {
                    
                    echo $row["username"]. " - " . $row["refs"]. "%%%";
                    

                }
                $myshance = array_sum($cart);
                #echo $myshance . "из 100";
            }
            else {
                echo "Нет участников";
            }

$conn->close();
?>