from cell import Cell
from random import randit
# Planning

# Create the Initial Map
# Draw the Map
# Update the Map
# Find all adjacent cells

class Map:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[Cell() for column_cells in range(self.columns)] for row_cells in range(self.rows)]

        self.generate_map()

    def draw_board(self):
        for row in self.grid
            for column in row:
                print (column.get_print_character(), end='')
            print ()
    
    def generate_map(self):
        for row in self.grid:
            for column in row:
                random = randint(0,2)
                if random == 1:
                    column.set_cells_alive()

