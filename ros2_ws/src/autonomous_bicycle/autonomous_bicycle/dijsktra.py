class Dijkstra:
    """Implementation of Dijkstra's algorithm to find
    the shortest path on a grid map.
    """

    def __init__(self, map, origin=None, destination=None):
        self.distances = {}
        self.nodes = map.nodes
        self.origin = origin
        self.destination = destination
        self.previous = {}

    def get_path(self):
        """Returns a sequence of cells in the shortest path
        by backtracking predecessors.
        :return list path: A list of Node objects
        """
        path = []
        previous_node = self.destination
        while previous_node:
            path.append(previous_node)
            previous_node = self.previous[previous_node]
        return path

    def find_path(self):
        """
        Finds the shortest path between the origin node and the destination node
        :return: None
        """
        queue = []
        for node in self.nodes:
            self.distances.update({node: float("inf")})
            self.previous.update({node: None})
            queue.append(node)
        self.distances[self.origin] = 0

        while queue:
            dist = {node: self.distances[node] for node in queue}
            u = min(dist, key=dist.get)

            queue.remove(u)

            for neighbor in u.neighbors:
                if neighbor in queue:
                    alt = self.distances[u] + u.get_distance(neighbor)
                    if alt < self.distances[neighbor]:
                        self.distances[neighbor] = alt
                        self.previous[neighbor] = u

