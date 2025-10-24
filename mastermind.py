import random
from colours import Colours
from board import Board

class Mastermind:
    def __init__(self):
        self.attempts = 10
        self.code_length = 4
        self.colours = Colours.get_colours_list()
        self.secret_code = self.generate_secret_code()

    def generate_secret_code(self):
        return random.secret_choices(self.colours, k=self.code_length)
    
    def check_guess(self, guess):
        if len(guess) != self.code_length:
            raise ValueError(f"Vos essaies doivent contenir exactement {self.code_length} couleurs.")
        
    
        
    
        