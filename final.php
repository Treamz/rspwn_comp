<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Comp#1</title>
    <link rel="stylesheet" href="main.css">
</head>
<body>
<div class="container">
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


            $sql = "SELECT username, refs FROM rspwn_comp1 WHERE refs > 0";
            $result = $conn->query($sql);
            $cart = array();
            if ($result->num_rows > 0) {
                while($row = $result->fetch_assoc()) {
                    #echo "username: " . $row["username"]. " - refs: " . $row["refs"]. "<br>";
                    for ($i=0; $i< $row["refs"];$i++) {
                         array_push($cart,$row["username"]);
                    }

                }
                #echo json_encode($cart);
                $count = count($cart);
                shuffle($cart);
                for($i = 0; $i < $count; $i++) {
                    $n = $i + 1;
                    echo '<div class="item">'. ($n) ." ". ($cart[$i]) . '</div>';
                }
            }
            else {
                echo "Eroro";
            }
$conn->close();
?>
</div>
</body>
</html>