import math
import random

class Player:
    def __init__(self,letter):
        self.letter = letter

    # we want all player to get move
    def get_move(self,game):
        pass


#inherit from player class
class RandoemComputer(Player):
    def __init__ (self, letter):
        super().__init__(letter)
    # for computer , computer will choose randome move
    def get_move(self, game):
        randome_move = random.choice(game.get_empty_squares())
        return randome_move


class HumanPlayer(Player):
    def __init__ (self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        vol = None
        while not valid_square:
            sq =  input( self.letter + " choose a square: ")
            # we are going to check if the input is valid or not and if the space is available
            # if input is not valid we will say not valid input
            # is the space is not available we will say the space is not available
            try:
                vol = int(sq)
                if not vol <= 9 and vol >= 0:
                    raise ValueError("Not valid input")
                if vol not in game.get_empty_squares():
                    raise ValueError("Space is not available")
                valid_square = True
            except ValueError as e:
                print(e)
        return vol