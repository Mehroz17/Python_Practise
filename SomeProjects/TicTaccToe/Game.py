import time


class TicTacToe:
    def __init__(self):
        self.board = [" " for i in range(9)] # making an board for game the board has 9 square so the range will be 9
        self.current_winner = None # current winner is none at the beginning

    #printing the board function
    def print_board(self):
        for row in [self.board[i*3:i*3+3] for i in range(3)]:
            print("| "+ ' | '.join(row)+' |')



    @staticmethod
        # this method tell which number corespond to which square
    def print_board_nums():
        number  = [[str(i) for i in range(j * 3, j * 3 + 3)] for j in range(3)]
        for row in number:
            print("| "+ ' | '.join(row)+' |')


    # we want to know the empty spaces to get our move next
    def get_empty_squares(self):
        return [i for i, square in enumerate(self.board) if square == " "]


    def empty_square(self):
        return ' ' in self.board


    def make_move(self,square,letter):
        if(self.board[square] == ' '):
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False

    def winner(self,square , letter):
        row_idx = square // 3
        row = self.board[row_idx * 3:(row_idx + 1) * 3]
        if all(spot == letter for spot in row):
            return True

        #check column
        col_idx = square % 3
        column = [self.board[col_idx + i * 3] for i in range(3)]
        if all(spot == letter for spot in column):
            return True

        #check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all(spot == letter for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all(spot == letter for spot in diagonal2):
                return True
        return False




def play(game , x_player , o_player, print_game = True):
    if print_game:
        game.print_board_nums()

    letter = "X" #starting letter
    # iterate the game until there is not empty spaces
    while game.empty_square():
        if letter == "X":
            move = x_player.get_move(game)
        else:
            move = o_player.get_move(game)

        if game.make_move(move,letter):
            if print_game:
                print(letter + f" moved to square {move}" )
                game.print_board()
                print(" ")
            if game.current_winner:
                if print_game:
                    print(letter + " wins!")
                return letter
            time.sleep(1.0)
            letter = "X" if letter == "O" else "O"

    if print_game:
        print("It's a tie!")



# calling the game
# as the human player are in the player
# so we have to call them from player class
from player import HumanPlayer,RandoemComputer
def paly_game():
    xp = HumanPlayer("X")
    op = HumanPlayer("O")
    t  = TicTacToe()
    play(t,xp,op,print_game=True)

paly_game()