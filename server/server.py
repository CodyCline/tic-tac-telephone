from flask import Flask, request, render_template
from flask_socketio import SocketIO, join_room, emit, send
from flask_cors import CORS
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from twilio.twiml.voice_response import VoiceResponse, Gather
from games import tic_tac_toe

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
game_lobbies = {***REMOVED*** # dict to track active rooms
# client = Client()

@app.route('/')
def index():
    #Index html debug page
    return render_template('index.html')


@socketio.on('create')
def on_create():
    #Create lobby
    game = tic_tac_toe.Game(
        player=""
    )
    room_id = game.generate_room_id()
    join_room(room_id)
    game_lobbies[room_id] = game
    emit('game_created', {'room': room_id***REMOVED***


#This will likely be used only for re-entering lost room
@socketio.on('join')
def on_join(data):
    #Join the game lobby after creation if it exists.
    room = data['roomId']
    if room in game_lobbies:
        join_room(room)
        send(game_lobbies[room], room=room)
    else:
        emit('error', {'error': 'Unable to join room. Room does not exist.'***REMOVED***

# @socketio.on('make_move')
def make_move(data):
    room = data['room_id']
    game = game_lobbies[room]
    if room in game_lobbies: #If game exists
        player_move = int(data['player_move'])
        #Make player move, computer follows, check for winner. Send appropriate data back to client
        game.make_move(player_move, 'X')
        if game.check_winner('X'):
            #Send win message, log the win to the database
            socketio.emit('updateBoard', {
                'board': game.get_board()
            ***REMOVED***
            socketio.emit('winner', 'PLAYER WINS')
        elif game.check_winner('O'):
            socketio.emit('updateBoard', {
                'board': game.get_board()
            ***REMOVED***
            socketio.emit('winner', 'CPU WINS')
        else:
            game.computer_move()
            game.get_board()
            socketio.emit('updateBoard', {
                'board': game.get_board()
            ***REMOVED***
    else:
        emit('error', {'bad_request': '400'***REMOVED***


@app.route("/start", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls with a menu of options"""
    # Start our TwiML response
    resp = VoiceResponse()
    
    # Start our <Gather> verb
    gather = Gather(num_digits=1, action='/gather')
    gather.say('Welcome to tic-tac-telephone.')
    resp.append(gather)
    # If the user doesn't select an option, redirect them into a loop
    resp.redirect('/start')

    return str(resp)


#Verify phone number before initiating game
@app.route('/verify', methods=['GET', 'POST'])
def verify(data):
    try:
        #Return true if number is not a voip or business type
        response = client.lookups.phone_numbers(data.phoneNumber).fetch()
        if(response):
            return ({"status": "verified"***REMOVED***
    #Return false if doesn't exist
    except TwilioRestException as e:
        if e.code == 20404:
            return False
        else:
            raise e

@app.route('/gather', methods=['GET', 'POST'])
def gather():
    """Processes results from the <Gather> prompt in /voice"""
    # Start our TwiML response
    resp = VoiceResponse()

    # If Twilio's request to our app included already gathered digits,
    # process them
    if 'Digits' in request.values:
        # Get which digit the caller chose
        choice = request.values['Digits']

        # <Say> a different message depending on the caller's choice
        if choice == '1':
            make_move({'room_id': '123', 'player_move': 0***REMOVED***
            resp.say('You chose 1')
        elif choice == '2':
            make_move({'room_id': '123', 'player_move': 1***REMOVED***
            resp.say('You chose 2')
        elif choice == '3':
            make_move({'room_id': '123', 'player_move': 2***REMOVED***
            resp.say('You chose 3')
        elif choice == '4':
            make_move({'room_id': '123', 'player_move': 3***REMOVED***
            resp.say('You chose 4')
        elif choice == '5':
            make_move({'room_id': '123', 'player_move': 4***REMOVED***
            resp.say('You chose 5')
        elif choice == '6':
            make_move({'room_id': '123', 'player_move': 5***REMOVED***
            resp.say('You chose 6')
        elif choice == '7':
            make_move({'room_id': '123', 'player_move': 6***REMOVED***
            resp.say('You chose 7')
        elif choice == '8':
            make_move({'room_id': '123', 'player_move': 7***REMOVED***
            resp.say('You chose 8')
        elif choice == '9':
            make_move({'room_id': '123', 'player_move': 8***REMOVED***
            resp.say('You chose 9')
        else:
            # If the caller didn't choose 1 or 2, apologize and ask them again
            resp.say("Sorry, I don't understand that choice.")

    # If the user didn't choose 1 or 2 (or anything), send them back to /voice
    resp.redirect('/start')
    return str(resp)

if __name__ == '__main__':
    socketio.run(app, debug=True)