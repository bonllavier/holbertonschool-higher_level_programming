$(function()
{
  $.get("https://fourtonfish.com/hellosalut/?lang=fr", function(data)
	{
	  console.log(data);
	  $('DIV#hello').append(data.hello);
	  });
});
