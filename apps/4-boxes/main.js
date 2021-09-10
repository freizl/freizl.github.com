$(function () {

  $('.boxes > div').click(function () {
    var $that = $(this),
        $parent = $that.parent(),
        bgColor = $that.css('background-color');
    $parent.css('background-color', bgColor);
  });

});
