<!DOCTYPE html>
<html lang="en">
<head>
  <title>Home</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>

<div class="container">
  <h2>First form</h2>
  <form action="" method="POST">
      {{ csrf_field()}}
    <div class="form-group">
      <label for="email">From Date:</label>
      <input type="date" class="form-control" id="fdate" placeholder="Enter Date" name="fdate">
    </div>
    <div class="form-group">
      <label for="pwd">To Date:</label>
      <input type="date" class="form-control" id="tdate" placeholder="Enter To Date" name="tdate">
    </div>

    <button type="submit" class="btn btn-default">Submit</button>
  </form>
</div>

</body>
</html>
