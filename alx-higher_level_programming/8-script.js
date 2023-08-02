/*
JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
*/
$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      for (let i = 0; i < data.results.length; i++) {
        const title = data.results[i].title;
        $('#list_movies').append('<li>' + title + '</li>');
      }
    },
    error: function (xhr, status, error) {
      console.log('Error fetching movies data:', error);
    }
  });
});
