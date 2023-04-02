from node import Node

class Map:
    def __init__(self, size):
        self.size = size
        self.nodes = {}
        for i in range(size):
            for j in range(size):
                node = Node(i, j, False)
                self.nodes[i,j] = node
        
        node1 = Node(0,2,True)
        self.nodes[0,2] = node1

        node2 = Node(1,5,True)
        self.nodes[1,5] = node2
        
        node3 = Node(1,7,True)
        self.nodes[1,7] = node3
        
        node4 = Node(3,1,True)
        self.nodes[3,1] = node4
        
        node5 = Node(3,4,True)
        self.nodes[3,4] = node5
        
        node6 = Node(4,8,True)
        self.nodes[4,8] = node6
        
        node7 = Node(5,5,True)
        self.nodes[5,5] = node7
        
        node8 = Node(6,2,True)
        self.nodes[6,2] = node8
        
        node9 = Node(7,7,True)
        self.nodes[7,7] = node9
        
        node10 = Node(9,2,True)
        self.nodes[9,2] = node10
        
    
    def find_neighbors(self, node):
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                neighbor_x = node.pos_x + i
                neighbor_y = node.pos_y + j
                if neighbor_x < 0 or neighbor_x >= self.size or neighbor_y < 0 or neighbor_y >= self.size:
                    continue
                neighbor = self.nodes[neighbor_x, neighbor_y]
                if not neighbor.is_occupied:
                    neighbors.append(neighbor)
        return neighbors

    def get_nodes(self):
        return self.nodes
