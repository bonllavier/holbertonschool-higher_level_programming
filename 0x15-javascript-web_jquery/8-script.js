$(function()
{
  $.get("https://swapi.co/api/films/?format=json", function(data)
	{
	  console.log(data.results);
	  $.each(data.results, function(i, field){
	    $('UL#list_movies').append('<li>' + field.title + '</li>');
	    });
	  });
});
