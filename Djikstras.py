'''
The graph is defined by a 2D array.
The array can have obstacles which are represented with 'o'

'''
from array import *

#The lowest number that represents a valid coordinate
MIN = 0
#The largest X coordinate
MAX_X = 0
#The largest Y coordinate
MAX_Y = 0

class Graph:
    #Define the dimensions of the graph
    def __init__(self, dim_x, dim_y):
        self.cols, self.rows = (dim_x, dim_y)
        global MAX_X, MAX_Y
        MAX_X = dim_x
        MAX_Y = dim_y
        #Defining a 2D array with distances set as -1 (for infinitely long)
        #All adjascent coordinates are length 1 away
        self.graph = [[-1 for x in range(self.cols)] for y in range(self.rows)]

    def printGraph(self):
        for item in self.graph:
            print(item)

    def setPointAs(self, x_coord, y_coord, val):
        self.graph[y_coord][x_coord] = val

    def withinBounds(self, x_coord, y_coord):
        return (x_coord >= MIN and x_coord < MAX_X) and (y_coord >= MIN and y_coord < MAX_Y)
    #traverse a path diven the starting and ending position in the graph
    def traverse(self, x_start, y_start, x_end, y_end):
        if (not self.withinBounds(x_start, y_start)):
            raise ArithmeticError("Entered start coordinates exceeds map limits")
        if (not self.withinBounds(x_end, y_end)):
            raise ArithmeticError("Entered end coordinates exceeds map limits")
        #Make the map look more intuitive as to where the start and end are
        toSearch = [[(x, y) for x in range(0, MAX_X)] for y in range(0, MAX_Y)]
        prev     = [[(-1, -1) for x in range(0, MAX_X)] for y in range(0, MAX_Y)]
        self.setPointAs(x_start, y_start, 0) #Set distance to 0
        #Setup the queue -> Based on the position of the graph
        currQ    = set()
        Visited  = set()
        currQ.add((x_start, y_start))
        while len(currQ) > 0:
            (curr_x, curr_y) = currQ.pop()
            dist = self.graph[curr_y][curr_x] #Rows are defined first then the columns
            intPos = [[(intx, inty) for intx in range(curr_x-1, curr_x+2)]
                        for inty in range(curr_y-1, curr_y+2)]
            for coord in intPos:
                for pos in coord:
                    if (not self.withinBounds(pos[0], pos[1])): continue
                    print(pos[0], pos[1])

#Traversal algorithm
# Set of coordinates that represent the position not yet visited
if __name__ == "__main__":
    graph = Graph(16, 8)
    graph.traverse(0, 7, 5, 5)
