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
        //echo "username: " . $row["username"]. " - refs: " . $row["refs"]. "<br>";
        $myrefs = $row["refs"];
        if ($row["refs"] < 2) {
            echo "Нет шансов <br>";
        }
        else {
            //echo "Высчитываю <br>";
            $sql = "SELECT username, refs FROM rspwn_comp1 WHERE refs > 1";
            $result = $conn->query($sql);
            $cart = array();
            if ($result->num_rows > 0) {
                while($row = $result->fetch_assoc()) {
                    //echo "username: " . $row["username"]. " - refs: " . $row["refs"]. "<br>";
                    for ($i=0; $i< $row["refs"];$i++) {
                         array_push($cart,$row["refs"]);
                    }

                }
                //echo json_encode($cart);
               // echo $myrefs;
                //echo "sum(a) = " . array_sum($cart) . "\n";
                $myshance = ($myrefs / count($cart)) * 100;
                #echo $myshance ." ". $myrefs . "%%%";
                echo $myshance . "%%%". $myrefs . "%%%";
            }
        }

    }
} else {
    echo "0 results";
}
$conn->close();
?>