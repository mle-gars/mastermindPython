class Colours:
    def __init__(self, red, green, blue, yellow, white, black):
        self.red = red
        self.green = green 
        self.blue = blue
        self.yellow = yellow
        self.white = white
        self.black = black

    # Methode pour obtenir la liste des couleurs disponibles
    def get_colours_list(self):
        return [self.red, self.green, self.blue, self.yellow, self.white, self.black]
    
    # Representation de l'objet Colours pour l'affichage. 
    # Etait ce nécessaire pour afficher les couleurs disponibles dans mastermind.py ?
    def __repr__(self):
        return f"Colours available: {self.red}, {self.green}, {self.blue}, {self.yellow}, {self.white}, {self.black}"
    
colours_instance = Colours('Red', 'Green', 'Blue', 'Yellow', 'White', 'Black')


