"""
Clone of 2048 game.
"""

import poc_2048_gui        

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    

OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    temp = [value for value in line if value!= 0]
    temp.extend([value for value in line if value==0])
    
    for i in range(len(temp) - 1):
        if temp[i]== temp[i+1]:
            temp[i] = temp[i] + temp[i+1]
            temp.pop(i + 1)
            temp.append(0)
#    for i in range(len(temp) - 1):
#        temp[i] = temp[i] * 2
#        temp.pop(i + 1)
#        temp.append(0)
    
#     replace with your code
    return temp

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._col = grid_height
        self._row = grid_width        
        self._grid= []
        self.reset()
    
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        # replace with your code
        self._grid = [[0 for dummy_cols in range(self._col)] for dummy_row in range(self._row)]
        
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return self_grid

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._col
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self_row
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        pass
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        # replace with your code
        self._grid[col][row] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        # replace with your code
        return self._grid[row][col]
 
    
#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

print merge([2, 0, 2, 4])
print merge([0, 0, 2, 2])
print merge([2, 2, 0, 0])
print merge([2, 2, 2, 2])
print merge([8, 16, 16, 8])


