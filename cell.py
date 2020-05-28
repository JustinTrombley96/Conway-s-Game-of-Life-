# Planning

# Initialize the Map
# Set Cells to Alive
# Set Cells to Dead
# Check if the Cell is Alive 

class Cell:
    def __init__(self):
        self.status = 'Dead'
    def set_cells_alive(self):
        self.status = 'Alive'
    def set_cells_dead(self):
        set.status = 'Dead'
    def cell_check(self):
        if self.status == 'Alive':
            return True
        return False
        