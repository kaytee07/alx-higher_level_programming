/*
JavaScript script that fetches and prints how to say “Hello” depending on the language

You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
The translation must be fetched when the user clicks on INPUT#btn_translate
The translation of “Hello” must be displayed in the HTML tag DIV#hello
You can’t use document.querySelector to select the HTML tag
*/
$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $('#btn_translate').click(function () {
    $.get(url + $.param({ lang: $('#language_code').val() }), function (data) {
      $('#hello').html(data.hello);
    });
  });
});
