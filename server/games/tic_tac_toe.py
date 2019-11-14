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

    def computer_move(self, boardState):
        pass

    def is_winner(self, board, letter):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use board instead of board and letter instead of letter so we don't have to type as much.
        return (
            (board[7] == letter and board[8] == letter and board[9] == letter) or # across the top
            (board[4] == letter and board[5] == letter and board[6] == letter) or # across the middle
            (board[1] == letter and board[2] == letter and board[3] == letter) or # across the bottom
            (board[7] == letter and board[4] == letter and board[1] == letter) or # down the left side
            (board[8] == letter and board[5] == letter and board[2] == letter) or # down the middle
            (board[9] == letter and board[6] == letter and board[3] == letter) or # down the right side
            (board[7] == letter and board[5] == letter and board[3] == letter) or # diagonal
            (board[9] == letter and board[5] == letter and board[1] == letter)
        ) # diagonal

    @classmethod
    def generate_room_id(cls):
        #Generate random room id
        id_length = 6
        return ''.join(random.SystemRandom().choice(
            string.ascii_uppercase) for _ in range(id_length))