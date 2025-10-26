import random
from colours import Colours

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
        for colour in guess:
            if colour not in self.colours:
                raise ValueError(f"La couleur '{colour}' n'est pas valide. Choisissez parmi : {', '.join(self.colours)}")
            if colour in self.secret_code:
                print(f"La couleur '{colour}' est correcte.")
                if guess.index(colour) == self.secret_code.index(colour):
                    print(f"La couleur '{colour}' est à la bonne position.")
                    self.secret_code[self.secret_code.index(colour)] = None
                    guess[guess.index(colour)] = None
            if guess == self.secret_code:
                break

            
        
    def play(self):
        print("Bienvenue dans Mastermind!")
        print("Les couleurs disponibles sont :")
        for colour in self.colours:
            print(f"- {colour}")
        print(f"Vous devez deviner le code secret composé de {self.code_length} couleurs. Vous avez {self.attempts} tentatives.")

        while self.attempts > 0:
            guess = input("Entrez votre proposition : ").split()
            try:
                self.check_guess(guess)
            except ValueError as e:
                print(e)
                continue

            if guess == self.secret_code:
                print("Félicitations ! Vous avez deviné le code secret.")
                return

            self.attempts -= 1
            print(f"Il vous reste {self.attempts} tentatives.")

        print(f"Vous avez perdu ! Le code secret était : {self.secret_code}")

