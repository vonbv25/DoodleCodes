"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import math
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = "obstacle"
HUMAN = "human"
ZOMBIE = "zombie"


class Zombie(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row,col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row,col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes a 2D distance field
        Distance at member of entity_queue is zero
        Shortest paths avoid obstacles and use distance_type distances
        """
        
        visited_grid = poc_grid.Grid(self.get_grid_height(),self.get_grid_width())
        
        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                if not self.is_empty(row, col):
                    visited_grid.set_full(row, col) 
                    
        distance_field = [[self.get_grid_width() * self.get_grid_height()  \
                           for dummy_cols in range(self.get_grid_width())]\
                   for dummy_rows in range(self.get_grid_height())]
        
        boundary = poc_queue.Queue()
        
        if (entity_type== HUMAN):
            for human in self.humans():
                boundary.enqueue(human)
        elif(entity_type== ZOMBIE):
            for zombie in self.zombies():
                boundary.enqueue(zombie)
        
        for entity in boundary:
            distance_field[entity[0]][entity[1]] = 0
            visited_grid.set_full(entity[0],entity[1])
         
        while len(boundary)> 0:
            cell = boundary.dequeue()
            neighbors = self.four_neighbors(cell[0],cell[1])
            for neighbor in neighbors:
                if visited_grid.is_empty(neighbor[0],neighbor[1]):
                    distance_field[neighbor[0]][neighbor[1]] = min(distance_field[neighbor[0]][neighbor[1]], \
                                         distance_field[cell[0]][cell[1]] + 1)
                    visited_grid.set_full(neighbor[0],neighbor[1])
                    boundary.enqueue(neighbor)
        return distance_field           
     
        
    
    def move_humans(self, zombie_distance):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        index =  0
        temp_human_list = self._human_list
        for human in temp_human_list:
            safe_pos = human
            safe_distance = zombie_distance[human[0]][human[1]]
            
            neighbors = self.eight_neighbors(human[0],human[1])
            
            for neighbor in neighbors:
                if self.is_empty(neighbor[0],neighbor[1]):
                    distance = zombie_distance[neighbor[0]][neighbor[1]]
                    if safe_distance < distance:
                        safe_distance = distance
                        safe_pos = neighbor
            self._human_list[index] = safe_pos
            index = index+ 1
                    
        
        
    
    def move_zombies(self, human_distance):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        index =  0
        temp_zombie_list = self._zombie_list
        for zombie in temp_zombie_list:
            target_pos = zombie
            nearest_distance = human_distance[zombie[0]][zombie[1]]
            
            neighbors = self.four_neighbors(zombie[0],zombie[1])
            
            for neighbor in neighbors:
                if self.is_empty(neighbor[0],neighbor[1]):
                    distance = human_distance[neighbor[0]][neighbor[1]]
                    if nearest_distance > distance:
                        nearest_distance = distance
                        target_pos = neighbor
            self._zombie_list[index] = target_pos
            index = index+ 1

        

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Zombie(30, 40))
