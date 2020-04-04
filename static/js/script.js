function card_path(card_name) {
  return "/static/images/" + card_name + ".png"
};

function game_rerender(game_state) {

  // console.log(game_state);
  $('#content').empty();

  for (var i = 0; i < game_state.players.length; i++) {
    let player = game_state.players[i];
    $('#content').append(player);
    $('#content').append("<br>");
    if (game_state.hands[player]) {
      player_hand = game_state.hands[player].length !== 0 ? JSON.parse(game_state.hands[player]) : [];
      for (var j = 0; j < player_hand.length; j++) {
        $('#content').append('<img src=' + card_path(player_hand[j]) + ' style="height: 200" />');
      }
      $('#content').append("<br>");
    }
  }

};

// rerender every second
$( document ).ready(function() {
  setInterval(function(){
    $.post('get_game_state', function(game_state) {
      game_rerender(JSON.parse(game_state));
    });
  }, 1000);
});
