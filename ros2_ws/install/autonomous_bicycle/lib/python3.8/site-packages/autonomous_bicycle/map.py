from autonomous_bicycle.node import Node
class Map:

    def __init__(self, size):
        self.size = size;
        self.lst = [[] for _ in range(size)];
        self.nodes = [];

    def find_neighbors(self, node):
        neighbors = [];
        i = node.pos_x;
        j = node.pos_y;
    

        if(i != 0):                               # N
            neighbors.append(self.lst[i - 1][j]);
        if(i != (self.size - 1)):                 # S
            neighbors.append(self.lst[i + 1][j]);
        if(j != 0):                               # W
            neighbors.append(self.lst[i][j - 1]);
        if(j != (self.size - 1)):                 # E
            neighbors.append(self.lst[i][j + 1]);
    
        if(i != 0 and j != 0):                              # NW
            neighbors.append(self.lst[i - 1][j - 1]);
        if(i != 0 and j != (self.size - 1)):                # NE
            neighbors.append(self.lst[i - 1][j + 1]);
        if(i != (self.size - 1) and j != 0):                # SW
            neighbors.append(self.lst[i + 1][j - 1]); 
        if(i != (self.size - 1) and j != (self.size - 1)):  # SE
            neighbors.append(self.lst[i + 1][j + 1]);
    

        return neighbors;
        


    def get_nodes(self):
        occupied = [[0, 2], [1, 5], [1, 7], [3, 1], [3, 4], [4, 8], [5, 5], [6, 2], [7, 7], [9, 2]]; # Buildings on map
        # occupied = [[0, 2], [1, 5], [1, 7], [3, 1], [3, 4], [4, 8], [6, 2], [9, 2]];
        
        for i in range(0, self.size):
            for j in range(0, self.size):
                node = Node(i, j, False, []);

                if([i, j] in occupied):
                    node.set_occupancy(True);

                self.lst[i].append(node);

        for i in range(len(self.lst)):
            for node in self.lst[i]:
                node.set_neighbors(self.find_neighbors(node));
                self.nodes.append(node);


        return self.nodes;   
