$(document).ready(function()) {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    var movies = data.results;
    var list = $('#list_movies');
    
    $.each(movies, function(index, movie) {
      var title = $('<li>').text(movie.title);
      list.append(title);
    });
  });
});
