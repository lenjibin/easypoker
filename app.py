import os, json, random

from flask import Flask, render_template


# create and configure the app
app = Flask(__name__)

game_state = {
    "cards": ['AC', 'AD', 'AS', 'AH', '2C', '2D', '2S', '2H', '3C', '3D', '3S', '3H', '4C', '4D', '4S', '4H', '5C', '5D', '5S', '5H', '6C', '6D', '6S', '6H', '7C', '7D', '7S', '7H', '8C', '8D', '8S', '8H', '9C', '9D', '9S', '9H', '10C', '10D', '10S', '10H', 'JC', 'JD', 'JS', 'JH', 'QC', 'QD', 'QS', 'QH', 'KC', 'KD', 'KS', 'KH'],
}

# a simple page that says hello
@app.route('/')
def hello():
    return render_template('hello.html', game_state=game_state)

@app.route('/add_player/<username>')
def add_player(username):
    game_state[username] = "la"
    return "successfully added " + username

@app.route('/get_random_card', methods=['POST'])
def get_random_card():
    return random.choice(game_state["cards"])

@app.route('/get_card/<card_name>', methods=['POST'])
def get_card(card_name):
    return "/static/images/" + card_name + ".png"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
