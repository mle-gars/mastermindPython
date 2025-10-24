# mastermind board class
class Board:
    def __init__(self, columns, lines):
        self.columns = columns
        self.lines = lines
        self.grid = [[' ' for _ in range(columns)] for _ in range(lines)]

    def __repr__(self):
        return f"Grid /n {self.grid}"
    
    def display_board(self):
        for row in self.grid:
            print('| ' + ' | '.join(row) + ' |')
            print('-' * (self.columns * 4 + 1))
    

