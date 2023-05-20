import random
import math

class player:
    def __init__(self,letter) -> None:
        self.letter = letter
    
    def get_move(self,game):
        pass

class random_computer(player):
    def __init__(self, letter) -> None:
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class human_player(player):
    def __init__(self, letter) -> None:
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square :
            square = input(self.letter + '\'s turn. input a square from(0 to 8): ')
            try:
                val = int(square)
                if val not in game.available_moves() :
                    raise ValueError
                valid_square = True
            except:
                print('invalid square')  
        return val 