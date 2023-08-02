/*
JavaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hell
*/
$(document).ready(function () {
  $.ajax({
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      $('#hello').text(data.hello);
    },
    error: function (xhr, status, error) {
      console.log('Error fetching translation:', error);
    }
  });
});
