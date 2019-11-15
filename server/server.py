from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit, send
from games import tic_tac_toe

# initialize Flask
app = Flask(__name__)
socketio = SocketIO(app)
game_lobbies = {***REMOVED*** # dict to track active rooms

@app.route('/')
def index():
    #Index html debug page
    return render_template('index.html')

@app.route('/call')
def inbound_call():
    #Handle inbound call and gather dialpad input
    return ''

@socketio.on('create')
def on_create(data):
    #Create lobby
    game = tic_tac_toe.Game(
        player=""
    )
    room_id = game.game_id
    join_room(room_id)
    game_lobbies[room_id] = game
    emit('join_room', {'room': room_id***REMOVED***


@socketio.on('join')
def on_join(data):
    #Join the game lobby after creation if it exists.
    room = data['room_id']
    if room in game_lobbies:
        join_room(room)
        send(game_lobbies[room], room=room)
    else:
        emit('error', {'error': 'Unable to join room. Room does not exist.'***REMOVED***

@socketio.on('make_move')
def make_move(data):
    print(data)
    room = data['room_id']
    game = game_lobbies[room]
    if room in game_lobbies: #If game exists
        player_move = int(data['player_move'])-1
        #Make player move, computer follows, check for winner. Send appropriate data back to server
        game.make_move(player_move, 'X')
        if game.check_winner('X'):
            #Send win message, log the win to the database
            emit('winner', 'PLAYER WINS')
        elif game.check_winner('O'):
            emit('winner', 'CPU WINS')
        else:
            game.computer_move()
            game.get_board()
            emit('update_board', {
                'board': game.get_board()
            ***REMOVED***
    else:
        emit('error', {'bad_request': '400'***REMOVED***

if __name__ == '__main__':
    socketio.run(app, debug=True)