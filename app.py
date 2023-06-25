from flask import Flask, render_template, request

app = Flask(__name__)

# Game state variables
player_x = 0
player_y = 0

@app.route('/')
def index():
    return render_template('game.html', x=player_x, y=player_y)

@app.route('/move', methods=['POST'])
def move():
    global player_x, player_y

    direction = request.form['direction']

    if direction == 'up':
        player_y -= 1
    elif direction == 'down':
        player_y += 1
    elif direction == 'left':
        player_x -= 1
    elif direction == 'right':
        player_x += 1

    return ''

if __name__ == '__main__':
    app.run(debug=True)
