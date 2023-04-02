from map import Map
from dijsktra import Dijkstra

def printmap(map):
    for i in range(10):
        print('\n+---+---+---+---+---+---+---+---+---+---+')
        for j in range(10):
            print('|', end = ' ')
            if (i == 0 and j == 0):
                print(' ', end = ' ')
            elif (i == 9 and j == 9):
                print('C', end = ' ')
            elif (map.nodes[i,j].is_occupied == False): 
                print(' ', end = ' ')
            else:
                print('O', end = ' ')
        print('|', end = ' ')
    print('\n+---+---+---+---+---+---+---+---+---+---+')

if __name__ == '__main__':
    map = Map(10)
    printmap(map)

    #origin = map.nodes[0,0]
    #destination = map.nodes[9,9]
    #nap = Dijkstra(map,origin,destination)
    #nap.get_path()
    #nap.find_path()