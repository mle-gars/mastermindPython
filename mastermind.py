import random
from colours import colours_instance

# Classe principale du jeu Mastermind 
# qui récupère les methodes de la classe Colours depuis colours.py
class Mastermind:
    def __init__(self):
        self.attempts = 10
        self.code_length = 4
        self.colours = colours_instance.get_colours_list()
        self.secret_code = self.generate_secret_code()

    #fonction qui me génère un code secret aléatoire grace aux couleurs disponibles danns colours.py avec 'random.choices'
    def generate_secret_code(self):
        return random.choices(self.colours, k=self.code_length)

    # Fonction qui vérifie la validité de la proposition du joueur 
    # et retourne les/des indices
    def check_guess(self, guess):
        # Je vérifie d'abord la validité de la proposition 
        # en comparant avec les couleurs disponibles et la longueur de la proposition
        if len(guess) != self.code_length:
            raise ValueError(f"Vos essais doivent contenir exactement {self.code_length} couleurs.")

        # Je vérifie que chaque couleur proposée est valide en itérant sur la proposition du jooueur
        for colour in guess:
            # Je vérifie que la couleur est bien dans la liste des couleurs disponibles
            if colour not in self.colours:
                raise ValueError(f"La couleur '{colour}' n'est pas valide.\n"
                                 f"Choisissez parmi : {', '.join(self.colours)}")

        # On calcule les indices
        # j'initialise les compteurs
        correct_position = 0
        correct_colour = 0
        # Je fais une copie du code secret et de la proposition du joueur pour les modifier sans affecter les originaux
        secret_code_copy = self.secret_code.copy()
        guess_copy = guess.copy()

        # Deux boucles 'for' à la suite 
        # pour identifier les couleurs correctes à la bonne position
        # et les couleurs correctes mais mal placées

        # D'abord, je compte les couleurs correctes à la bonne position
        # en itérant sur les indices de la longueur du code
        for i in range(self.code_length):
            # ensuite, je compare les couleurs aux mêmes indices 
            # dans le code secret et la proposition du joueur
            if guess_copy[i] == secret_code_copy[i]:
                # Si elles correspondent, j'incrémente le compteurr des bonnes position
                correct_position += 1
                # je marque ces positions comme déjà comptées en les remplaçant par 'None'
                secret_code_copy[i] = None
                # la même chose concernant la proposition du joueur
                guess_copy[i] = None

        # Ensuite, je compte les couleurs correctes mais mal placées
        for i in range(self.code_length):
            # Double vérification pour éviter de recompter les couleurs déjà identifiées.
            if guess_copy[i] is not None and guess_copy[i] in secret_code_copy:
                # Si la couleur proposée est dans le code secret (mais pas à la bonne position)
                # j'augmente le compteur
                correct_colour += 1
                # je marque cette couleur comme déjà comptée en la remplaçant par 'None'
                # Je modifie uniquement la première occurrence trouvée sans créer de liste temporaire.
                secret_code_copy[secret_code_copy.index(guess_copy[i])] = None

        # Je retourne les indices (bonne position && bonne couleur /
        # ou bonne couleur mais mal placée)
        return correct_position, correct_colour

    # Fonction principale pour jouer au jeu

    def play(self):
        print("Bienvenue dans Mastermind!")
        print(f"Les couleurs disponibles sont : {colours_instance}")
        print(f"Vous devez deviner le code secret composé de {self.code_length}\
                couleurs. Vous avez {self.attempts} tentatives.")

        # Boucle 'tant que' pour les tentatives du joueur
        while self.attempts > 0:
            # assez simple de compréhension (.split est nouveau pour moi = gestion des espaces)
            guess = input("Entrez votre proposition (séparées par des espaces) : ").split() 
            # pareil: try + except pour gérer les erreurs de saisie et implémenter la verif (nouveau pour moi)
            try:
                correct_position, correct_colour = self.check_guess(guess)
            except ValueError as e:
                print(e)
                continue

            # Vérification si le joueur a gagné ;)
            if guess == self.secret_code:
                print("Félicitations ! Vous avez deviné le code secret.")
                return

            print(f"Indices : {correct_position} couleur(s) correcte(s) à la bonne position (*),\
                                 {correct_colour} couleur(s) correcte(s) mais mal placée(s) (-).")
            
            self.attempts -= 1
            print(f"Il vous reste {self.attempts} tentatives.")

        print(f"Vous avez perdu ! Le code secret était : {self.secret_code}")

# appelle la classe et lance le jeu (nouvelle méthode magique inconnue : __main__)
if __name__ == "__main__":
    game = Mastermind()
    game.play()

# Merci à la chaine NeuralNine pour l'inspiration : cela m'a été d'un grand secours
# lors de mes bloacages sur ce projet.


