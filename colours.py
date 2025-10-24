class Colours:
    def __init__(self, red, green, blue, yellow, white, black):
        self.red = red
        self.green = green 
        self.blue = blue
        self.yellow = yellow
        self.white = white
        self.black = black

    def get_colours_list(self):
        return [self.red, self.green, self.blue, self.yellow, self.white, self.black]
    
    def __repr__(self):
        return f"Colours available: {self.red}, {self.green}, {self.blue}, {self.yellow}, {self.white}, {self.black}"
    
colours_instance = Colours('Red', 'Green', 'Blue', 'Yellow', 'White', 'Black')

print(colours_instance)
