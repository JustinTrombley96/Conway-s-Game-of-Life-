from PIL import Image
import os

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
        self.status = 'Dead'
    def is_alive(self):
        if self.status == 'Alive':
            return True
        return False
    def get_print_cell(self):
        if self.is_alive():
            # return '0'
            img = Image.open("alive_cell_20.png")
            return img.show()
        # return '.'
        dead_image = Image.open("dead_cell_20.png")
        dead_image.show()