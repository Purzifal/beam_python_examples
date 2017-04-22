<!DOCTYPE html>
<html>
  <head>
    <title>Beam Authentication Shortcode</title>
    <link rel="stylesheet" href="style.css">
   <link href='//fonts.googleapis.com/css?family=Orbitron' rel='stylesheet'>
  </head>
  <body>

    <div class="content">
      <img class="logo" src="/images/beam.png">
      <div class="code"><?php echo $_GET["code"]; ?></div>
      <div class="hint">Please copy the above shortcode in full and paste it into the app<br> This will allow it to connect to communicate with Beam's services</div>
    </div>
  </body>
</html>