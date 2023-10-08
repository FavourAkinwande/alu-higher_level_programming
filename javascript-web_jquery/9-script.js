// retrieves wind speed from api query
$(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data){
    $('#hello').text(data.hello);
  });
});
