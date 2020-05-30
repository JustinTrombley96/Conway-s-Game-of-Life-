class Table:
    def __init__(self):
        self.grid = [['TL', 'T', 'TR'],
                     ['L', 'M', 'R'],
                     ['BL', 'B', 'BR']]
    
    def print_grid(self):
        for row in self.grid:
            print(row)