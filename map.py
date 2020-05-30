from cell import Cell
from random import randint
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

    def draw_map(self):
        print('\n'*10)
        print()
        for row in self.grid:
            for column in row:
                print (column.get_print_cell(), end='')
            print ()
    
    def generate_map(self):
        for row in self.grid:
            for column in row:
                random = randint(0,2)
                if random == 1:
                    column.set_cells_alive()

    def update_map(self):
        goes_alive=[]
        gets_killed=[]

        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                check_neighbor = self.check_neighbor(row, column)

                living_neighbors_count = []

                for neighbor_cell in check_neighbor:
                    if neighbor_cell.is_alive():
                        living_neighbors_count.append(neighbor_cell)
                
                cell_object = self.grid[row][column]
                status_main_cell = cell_object.is_alive()

                if status_main_cell == True:
                    if len(living_neighbors_count) <2 or len(living_neighbors_count) > 3:
                        gets_killed.append(cell_object)
                    if len(living_neighbors_count) == 3 or len(living_neighbors_count) == 2:
                        goes_alive.append(cell_object)
                    
                else:
                    if len(living_neighbors_count) == 3:
                        goes_alive.append(cell_object)

            for cell_items in goes_alive:
                cell_items.set_cells_alive()
            for cell_items in gets_killed:
                cell_items.set_cells_dead()

    def check_neighbor(self, check_row, check_column):
        search_min = -1
        search_max = 2

        neighbor_list = []
        for row in range(search_min, search_max):
            for column in range(search_min, search_max):
                neighbor_row = check_row + row
                neighbor_column = check_column + column

                valid_neighbor = True

                if (neighbor_row) == check_row and (neighbor_column) == check_column:
                    valid_neighbor = False

                if (neighbor_row) < 0 or (neighbor_row) >= self.rows:
                    valid_neighbor = False
                
                if (neighbor_column) < 0 or (neighbor_column) >= self.columns:
                    valid_neighbor = False

                if valid_neighbor:
                    neighbor_list.append(self.grid[neighbor_row][neighbor_column])
        return neighbor_list
    

