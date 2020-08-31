<!DOCTYPE html>
<html lang="en">
<head>
  <title>Home</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
  <link rel="stylesheet" href="/resources/demos/style.css">
  <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
  <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
  <script>
    $( function() {
      $( "#fdate" ).datepicker({
        dateFormat: 'dd-mm-yy',
        maxDate: new Date()
      });
    } );
    $( function() {
      $( "#tdate" ).datepicker({
        dateFormat: 'dd-mm-yy',
        maxDate: new Date()
      });
    } );
    </script>
</head>
<body>

<div class="container">
  <h2>First form</h2>
  {{-- <div class="alert alert-success" role="alert">
    This is a success alert—check it out!
  </div> --}}
  @if(session('errors'))
  <div class="alert alert-danger" role="alert">
    {{session('errors')}}
  </div>
  @endif
  <form action="" method="POST">
      {{ csrf_field()}}
    <div class="form-group">
      <label for="email">From Date:</label>
      <input type="text" class="form-control" id="fdate" placeholder="Enter From Date" name="fdate">
    </div>
    <div class="form-group">
      <label for="pwd">To Date:</label>
      <input type="text" class="form-control" id="tdate" placeholder="Enter To Date" name="tdate">
    </div>

    <button type="submit" class="btn btn-default">Submit</button>
  </form>
</div>

</body>
</html>
