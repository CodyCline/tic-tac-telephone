import random, string

class Game:
    def __init__(self, player):
        self.game_id = self.generate_room_id()
        self.board=[' '] * 9
        self.player=player
        self.winner=None
        self.turn = None
        self.playing=False

    def get_board(self):
        return self.board

    def make_move(self, move, letter):
        self.board[move] = letter
    
    def is_space_free(self, move):
        return self.board[move] == ' '

    def computer_move(self):
        possible_moves = []
        for i in range(0, len(self.board)):
            if self.is_space_free(i):
                possible_moves.append(i)
        if len(possible_moves) != 0:
            return self.make_move(random.choice(possible_moves), 'O')
        else:
            return None
        

    def check_winner(self, letter):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use board instead of board and letter instead of letter so we don't have to type as much.
        board = self.board
        return (
            (board[6] == letter and board[7] == letter and board[8] == letter) or 
            (board[3] == letter and board[4] == letter and board[5] == letter) or 
            (board[0] == letter and board[1] == letter and board[2] == letter) or 
            (board[6] == letter and board[3] == letter and board[0] == letter) or 
            (board[7] == letter and board[4] == letter and board[1] == letter) or 
            (board[8] == letter and board[5] == letter and board[2] == letter) or 
            (board[6] == letter and board[4] == letter and board[2] == letter) or 
            (board[8] == letter and board[4] == letter and board[0] == letter)
        )

    @classmethod
    def generate_room_id(cls):
        #Generate random room id
        id_length = 6
        return ''.join(random.SystemRandom().choice(
            string.ascii_uppercase) for _ in range(id_length))