<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="author" content="Kiera Clarke">
        <title>Image Manipulation</title>
        <meta name="description" content="Manipulate images using Python">
        <link href="style.css" rel="stylesheet" type="text/css" media="screen" />
    </head>
    <body>
        <header>
            <h1>Image Manipulation</h1>
            <h3>Choose an image manipulation:</h3>
        </header>

        <div class="center-content">
            <img src="frosted-rose.jpg" alt="Frosted Rose" style="display: block; margin: 0 auto;">

            <form action="process.php" method="post">
                <label for="manipulation">Select Manipulation:</label>
                <select name="manipulation" id="manipulation">
                    <option value="flip">Flip</option>
                    <option value="mirror">Mirror</option>
                    <option value="invert">Invert</option>
                </select>
                <button type="submit" name="submit">Apply Manipulation</button>
            </form>

            <?php
            if (isset($_POST['submit'])) {
                $manipulation = $_POST['manipulation'];
                echo "Selected manipulation: $manipulation<br>";
                $output = shell_exec("python render.py $manipulation");
                echo "<p>Manipulation result: $output</p>";

                $imageFilename = $manipulation . '_image.jpg';
                echo "<img src='$imageFilename' alt='Manipulated Image' style='display: block; margin: 0 auto;'>";
            }
            ?>

        </div>
    </body>
</html>