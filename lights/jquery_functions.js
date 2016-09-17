$(document).ready(function() {
  $("#light1").click(function() {
    var f = !$(this).data("toggleFlag");
    if (f) {
      $(this).css('background-color', 'yellow');
      $(this).css('color', 'black');
      $(this).text("Light 1 On");
    } else {
      $(this).css('background-color', 'black');
      $(this).css('color', 'white');
      $(this).text('Light 1 Off');
    }
    $(this).data("toggleFlag", f);
  });
});
    
