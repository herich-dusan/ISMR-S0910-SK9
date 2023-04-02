from math import sqrt

class Node:

    def __init__(self, pos_x, pos_y, is_occupied, neighbors=None):
        self.pos_x = pos_x;
        self.pos_y = pos_y;
        self.is_occupied = is_occupied;
        self.neighbors = list(neighbors);
        

    def set_occupancy(self, is_occupied):
        self.is_occupied = is_occupied;

    # def get_occupancy(self):    
        # return self.is_occupied;

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors;

    def add_neighbor(self, neighbor):
        if not(neighbor in self.neighbors):
            self.neighbors.append(neighbor);

    def remove_neighbor(self, neighbor):
        if neighbor in self.neighbors:
            self.neighbors.remove(neighbor);

    def get_distance(self, node):
        if(node.is_occupied == True) or (self.is_occupied == True):
            return float("inf");
        
        return sqrt((self.pos_x-node.pos_x)**2 + (self.pos_y-node.pos_y)**2);
