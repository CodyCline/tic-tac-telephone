from flask import Flask, request, abort, jsonify
from flask_socketio import SocketIO, join_room, emit, send
from flask_cors import CORS, cross_origin
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Gather, Hangup
from twilio.base.exceptions import TwilioRestException
from config import server_config
from games import tic_tac_toe

env = server_config.DevelopmentSettings()
game_lobbies = {***REMOVED*** 
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')
CORS(app, resources={ r'/*': {'origins': env.CORS_CONFIG***REMOVED******REMOVED***
client = Client(env.TWILIO_ACCOUNT_SID, env.TWILIO_AUTH_TOKEN)


@socketio.on('create')
def on_create():
    #Create lobby
    print('creating')
    game = tic_tac_toe.Game(
        player=''
    )
    room_id = game.generate_room_id()
    # room_id = '123' #Debug
    join_room(room_id)
    game_lobbies[room_id] = game
    emit('GAME_CREATED', {'room': room_id***REMOVED***

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

#Check whether a game exists based on id
def game_exists(roomId):
    if roomId in game_lobbies:
        return True
    else:
        return False


def make_move(data):   
    room = data['room_id']
    if game_exists(room):
        game = game_lobbies[room]
        player_move = int(data['player_move'])
        #Make player move, computer follows, check for winner. Send appropriate data back to client
        game.make_move(player_move, 'X')
        if game.check_winner('X'):
            #Send win message. Todo log the win to the database
            socketio.emit('UPDATE_BOARD', {
                'board': game.get_board()
            ***REMOVED***
            socketio.emit('winner', 'PLAYER')
        else:
            game.computer_move()
            if game.check_winner('O'):
                socketio.emit('UPDATE_BOARD', {
                    'board': game.get_board()
                ***REMOVED***
                socketio.emit('winner', 'CPU')
            socketio.emit('UPDATE_BOARD', {
                'board': game.get_board()
            ***REMOVED***
    else:
        emit('error', {'bad_request': '400'***REMOVED***

@app.route('/game/<string:game_id>', methods=['GET', 'POST'])
@cross_origin()
def get_game(game_id):
    if game_exists(game_id):
        game = game_lobbies[game_id]
        return jsonify({'gameData': game.get_board()***REMOVED***
    else:
        abort(404)
    



#Ensure the phone number is real 
@app.route('/lookup', methods=['GET', 'POST'])
def lookup(phone):
    try:
        #Return true if number is not a voip or business type
        response = True
        if(response):
            return jsonify({'status': 'verified'***REMOVED***
    #Return false if doesn't exist
    except TwilioRestException as e:
        if e.code == 20404:
            return jsonify({'status': 'badNumber'***REMOVED***
        else:
            raise e
@app.route('/verify')
def verify():
    #should be 2fa authenticated in order to avoid spam or abuse
    pass

@socketio.on('start_call')
@app.route('/call')
def call(data):
    if data['roomid'] in game_lobbies: #If game exists
        client.calls.create(
            url='https://2dc85ece.ngrok.io/collect?roomid={***REMOVED***'.format(data['roomid']),
            to=data['phone'],
            from_=env.TWILIO_SERVER_PHONE
        )
        
    else:
        abort(400)



@app.route('/collect', methods=['GET', 'POST'])
def collect():
    '''Respond to incoming phone calls with a menu of options'''
    resp = VoiceResponse()
    gather = Gather(num_digits=1, action='/play?roomid={***REMOVED***'.format(request.args.get('roomid')))
    gather.say('Welcome to tic tac telephone. Use the keypad digits of 1-9 to play')
    resp.append(gather)
    # If the user doesn't select an option, redirect them into a loop
    resp.redirect('/collect')
    return str(resp)

@app.route('/play', methods=['GET', 'POST'])
def play():
    '''Processes results from the <Gather> prompt in /voice'''
    # Start our TwiML response
    print('ROOMIDS', request.args.get('roomid'))
    room_id = request.args.get('roomid')
    # room_id = 123
    resp = VoiceResponse()
    print('ROOM_ID', room_id)
    if 'Digits' in request.values:
        # Get which digit the caller chose
        choice = request.values['Digits']

        # <Say> a different message depending on the caller's choice
        if choice == '1':
            make_move({'room_id': room_id, 'player_move': 0***REMOVED***
            resp.say('You chose 1')
        elif choice == '2':
            make_move({'room_id': room_id, 'player_move': 1***REMOVED***
            resp.say('You chose 2')
        elif choice == '3':
            make_move({'room_id': room_id, 'player_move': 2***REMOVED***
            resp.say('You chose 3')
        elif choice == '4':
            make_move({'room_id': room_id, 'player_move': 3***REMOVED***
            resp.say('You chose 4')
        elif choice == '5':
            make_move({'room_id': room_id, 'player_move': 4***REMOVED***
            resp.say('You chose 5')
        elif choice == '6':
            make_move({'room_id': room_id, 'player_move': 5***REMOVED***
            resp.say('You chose 6')
        elif choice == '7':
            make_move({'room_id': room_id, 'player_move': 6***REMOVED***
            resp.say('You chose 7')
        elif choice == '8':
            make_move({'room_id': room_id, 'player_move': 7***REMOVED***
            resp.say('You chose 8')
        elif choice == '9':
            make_move({'room_id': room_id, 'player_move': 8***REMOVED***
            resp.say('You chose 9')
        else:
            # If the caller didn't choose 1 or 2, apologize and ask them again
            resp.say('Sorry, I don\'t understand that choice.')

    # If the user didn't choose 1 or 2 (or anything), send them back to /voice
    resp.redirect('/again?roomid={***REMOVED***'.format(request.args.get('roomid')))
    return str(resp)

@app.route('/again')
def turn():
    resp = VoiceResponse()
    resp.say('Go Again')


if __name__ == '__main__':
    socketio.run(app, debug=env.DEBUG)