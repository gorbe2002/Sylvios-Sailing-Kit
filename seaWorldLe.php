<?php
// Start the session to keep track of the game state
session_start();

function introduction() {
    echo "<p>Ahoy Mateys! Welcome to SeaWorldLE, enter a 5 letter sea-inspired word</p>";
}

function randomWord() {
    // Ensure the random word is only picked once per session
    if (!isset($_SESSION['wordle'])) {
        $words = file("seaWordBank.txt", FILE_IGNORE_NEW_LINES);
        $_SESSION['wordle'] = $words[array_rand($words)];
    }
    return $_SESSION['wordle'];
}

function resetGame() {
    // Reset the game by clearing the session variable
    unset($_SESSION['wordle']);
    unset($_SESSION['attempts']);
}

if (isset($_POST['reset'])) {
    resetGame();
}

$wordle = randomWord();
$won = false;
$guesses = $_SESSION['attempts'] ?? 0;

// Check if a guess was made
if (isset($_POST['guess'])) {
    $guesses++;
    $_SESSION['attempts'] = $guesses;
    $reckon = strtolower(substr(trim($_POST['guess']), 0, 5)); // Ensure guess is only 5 letters

    if ($reckon == $wordle) {
        $won = true;
        resetGame();
    } else if ($guesses >= 6) {
        resetGame();
    }
}
?>

<html>
<head>
    <link rel="stylesheet" href="wordle.css">
    <meta charset="UTF-8">
    <title>Wordle Game</title>
</head>
<body>
    <img class = 'leftCloud' src = 'clouds.png' height = 150 width = 150>
    <img class = 'rightCloud' src = 'clouds.png' height = 150 width = 150 >
    <?php introduction(); ?>
    <br>
    <br>
    
    <form method="post">
        <input type="text" name="guess" maxlength="5" minlength = "5" autocomplete="off" <?php if ($won || $guesses >= 6) echo 'disabled'; ?> required>
        <input type="submit" value="Guess" <?php if ($won || $guesses >= 6) echo 'disabled'; ?>>
        <input type="submit" name="reset" value="Reset">
    </form>
    
    <?php
    // Display the result of the guess
    if (isset($reckon) && !$won && $guesses < 6 ) {
        echo "<div>";
        for ($i = 0; $i < 5; $i++) {
            echo $reckon[$i] === $wordle[$i] ? "<span style='color:green;'>$reckon[$i]</span>" :
                 (strpos($wordle, $reckon[$i]) !== false ? "<span style='color:orange;'>$reckon[$i]</span>" :
                 "<span style='color:red;'>$reckon[$i]</span>");
        }
        echo "</div>";
    }

    if ($won) {
        echo "<p>ARR MATIE, YOU WON!!!!</p>";
    } else if ($guesses >= 6) {
        echo "<p> Sooo close, the word was " . $wordle . "</p>";
    }
    ?>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<img class ='waves' src = 'waves.png' height = 150 width = 1500>

</body>
</html>