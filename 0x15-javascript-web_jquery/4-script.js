var i=0;
$( "#toggle_header" ).click(function() {
  if (i == 0){
    $(this).removeClass( "green" ).addClass( "red" );
    i = 1;
    }
  else{
    $(this).removeClass( "red" ).addClass( "green" );
    i = 0;
    }
});
