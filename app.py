import os, json, random, copy

from flask import Flask, render_template


# create and configure the app
app = Flask(__name__)

game_state = {}
def reset_game():
    game_state["cards"] = ['AC', 'AD', 'AS', 'AH', '2C', '2D', '2S', '2H', '3C', '3D', '3S', '3H', '4C', '4D', '4S', '4H', '5C', '5D', '5S', '5H', '6C', '6D', '6S', '6H', '7C', '7D', '7S', '7H', '8C', '8D', '8S', '8H', '9C', '9D', '9S', '9H', '10C', '10D', '10S', '10H', 'JC', 'JD', 'JS', 'JH', 'QC', 'QD', 'QS', 'QH', 'KC', 'KD', 'KS', 'KH']
    game_state["players"] = []
    game_state["hands"] = {}
    game_state["money"] = {}
    game_state["table_cards"] = []
reset_game()

# game_cycle = [
#     "standby",
#     "deal",
#     "bet1",
#     "flop",
#     "bet2",
#     "turn",
#     "bet3",
#     "river",
#     "bet4",
#     "reveal",
# ]
# len_game_cycle = len(game_cycle)

@app.route('/')
def index():
    return render_template('game.html')

@app.route('/shuffle')
def shuffle():
    game_state["cards"] = ['AC', 'AD', 'AS', 'AH', '2C', '2D', '2S', '2H', '3C', '3D', '3S', '3H', '4C', '4D', '4S', '4H', '5C', '5D', '5S', '5H', '6C', '6D', '6S', '6H', '7C', '7D', '7S', '7H', '8C', '8D', '8S', '8H', '9C', '9D', '9S', '9H', '10C', '10D', '10S', '10H', 'JC', 'JD', 'JS', 'JH', 'QC', 'QD', 'QS', 'QH', 'KC', 'KD', 'KS', 'KH']
    game_state["hands"] = {}
    return "cards reset"

@app.route('/reset_everything')
def reset_everything():
    reset_game()
    return "everything reset"

@app.route('/get_game_state', methods=['GET', 'POST'])
def get_game_data():
    return json.dumps(game_state)

@app.route('/join/<username>')
def add_player(username):
    if username in game_state["players"]:
        return username + " is already in the game"
    game_state["players"].insert(random.randint(0, len(game_state["players"])), username)
    game_state["hands"][username] = []
    game_state["money"][username] = 0
    return "successfully added " + username

@app.route('/leave/<username>')
def remove_player(username):
    if username in game_state["players"]:
        game_state["players"].remove(username)
        game_state["hands"].pop(username)
        game_state["money"].pop(username)
        return "successfully removed " + username
    return username + " is not in the game"

@app.route('/give_money/<username>/<amount>')
def give_money(username, amount):
    if username not in game_state["players"]:
        return username + " is not in the game"
    if username in game_state["money"]:
        game_state["money"][username] += int(amount)
    else:
        game_state["money"][username] = int(amount)
    return "gave " + username + " " + amount + " dollars for a total of " + str(game_state["money"][username])

@app.route('/deal')
def deal():
    players_dealt_to = []
    for player in game_state["players"]:
        cards = get_random_card(2)
        game_state["hands"][player] = cards
        players_dealt_to.append(player)
    return "dealt cards to " + str(players_dealt_to)

@app.route('/draw_card', methods=['POST'])
@app.route('/draw_card/<num_cards>', methods=['POST'])
def get_random_card(num_cards=1):
    chosen_cards = []
    for i in range(int(num_cards)):
        chosen_card = random.choice(game_state["cards"])
        chosen_cards.append(chosen_card)
        game_state["cards"].remove(chosen_card)
    return json.dumps(chosen_cards)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
