/*JavaScript script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json*/
$(document).ready(function() {
  $.ajax({
    url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
    method: "GET",
    dataType: "json",
    success: function(data) {
      $("#character").text(data.name);
    },
    error: function(xhr, status, error) {
      console.log("Error fetching character data:", error);
    }
  });
});
