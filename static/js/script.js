$( document ).ready(function() {

  setInterval(function(){
    $.post('get_random_card', function(card) {
      $.post('get_card/'+card, function(card_path) {
        $('#card_placeholder').attr("src", card_path);
      });
    });
  }, 1000);

});
