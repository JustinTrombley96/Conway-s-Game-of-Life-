class Table:
    def __init__(self):
        self.grid = [['1', '2', '3'],
                     ['4', '5', '6'],
                     ['7', '8', '9']]
    
    def print_grid(self):
        for row in self.grid:
            print(row)