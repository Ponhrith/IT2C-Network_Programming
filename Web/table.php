<?php
include("fetch.php");
?>
<!DOCTYPE html>
<html>
<head>
  <!--link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"-->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
<div class="container">
 <div class="row">
   <div class="col-sm-8">
    <?php echo $deleteMsg??''; ?>
    <div class="table-responsive">
      <table class="table table-bordered">
       <thead><tr><th>Item</th>
         <th>Name</th>
         <th>Email</th>         
    </thead>
    <tbody>
  <?php
      if(is_array($fetchData)){      
      $item=1;
      foreach($fetchData as $data){
    ?>
      <tr>
      <td><?php echo $item; ?></td>
      <td><?php echo $data['NAME']??''; ?></td>
      
      <td><?php echo $data['EMAIL']??''; ?></td>
      </tr>
     <?php
      $item++;}}else{ ?>
      <tr>
        <td colspan="8">
    <?php echo json_encode($fetchData); ?>
  </td>
    <tr>
    <?php
    }?>
    </tbody>
     </table>
   </div>
</div>
</div>
</div>
</body>
</html>