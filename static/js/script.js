function game_rerender(game_state) {
  console.log(game_state);
  $.post('get_random_card', function(card) {
    $.post('get_card/'+card, function(card_path) {
      $('#card_placeholder').attr("src", card_path);
    });
  });
};

$( document ).ready(function() {
  setInterval(function(){
    $.post('get_game_state', function(game_state) {
      game_rerender(JSON.parse(game_state));
    });
  }, 1000);
});
