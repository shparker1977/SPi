$(document).ready(function() {
  $(".lightswitch").click(function() {
    var f = !$(this).data("toggleFlag");
    if (f) {
      $(this).css('background-color', 'yellow');
      $(this).css('color', 'black');
      $.post("/switchlight", {"lightNum": $(this).val()})
      .done()
    } else {
      $(this).css('background-color', 'black');
      $(this).css('color', 'white');
      $.post("/switchlight", {"lightNum": $(this).val()})
      .done()
    }
    $(this).data("toggleFlag", f);
  });
});
    
