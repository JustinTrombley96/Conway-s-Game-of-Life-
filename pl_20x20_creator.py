from PIL import Image 
import os

size_20 = (20, 20)

for f in os.listdir('.'):
    if f.endswith('.png'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.thumbnail(size_20)
        i.save('20/{}_20{}'.format(fn, fext))
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.thumbnail(size_20)
        i.convert('LA')
        i.save('20/{}_20.png'.format(fn, fext))
        
        
# alive_cell = Image.open('alive_block.png')
# dead_cell = Image.open('dead_block.jpg')
# alive_cell.show()
