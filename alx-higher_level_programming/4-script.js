/* JavaScript script that toggles the class of the <header>
  element when the user clicks on the tag */
$(document).ready(function () {
  $('#toggle_header').on('click', function () {
    $('header').toggleClass('red green');
  });
});
