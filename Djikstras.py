'''
The graph is defined by a 2D array.
The array can have obstacles which are represented with 'o'

'''
from array import *
import math

#The lowest number that represents a valid coordinate
MIN = 0
#The largest X coordinate
MAX_X = 0
#The largest Y coordinate
MAX_Y = 0
# A point is surrounded by 8 other elements therefore a point can be searched up
# to 8 times before it has been oversearched. This is not taking into account
# points that are on the corner which are only surrounded by 3 or points on the
# side which are only surrounded by 5
MAX_SEARCH = 8

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
        # 'NS' stands for NOT_SEARCHED, 'S' stands for SEARCHED
        toSearch = [[0 for x in range(0, MAX_X)] for y in range(0, MAX_Y)]
        prev     = [[(-1, -1) for x in range(0, MAX_X)] for y in range(0, MAX_Y)]
        self.setPointAs(x_start, y_start, 0) #Set distance to 0
        #Setup the queue -> Based on the position of the graph
        currQ    = set()
        currQ.add((x_start, y_start))
        while len(currQ) > 0:
            (curr_x, curr_y) = currQ.pop()
            dist = self.graph[curr_y][curr_x] #Rows are defined first then the columns
            intPos = [[(intx, inty) for intx in range(curr_x-1, curr_x+2)]
                        for inty in range(curr_y-1, curr_y+2)]
            for coord in intPos:
                for pos in coord:
                    (alt_x, alt_y) = pos
                    if (not self.withinBounds(alt_x, alt_y)): continue
                    if (toSearch[alt_y][alt_x] >= MAX_SEARCH): continue
                    currQ.add((alt_x, alt_y))
                    #Find the distance between the current position and the next
                    alt_dist = dist + math.sqrt(math.pow(alt_x-curr_x, 2) + math.pow(alt_y-curr_y, 2))
                    alt_dist = float("%.1f" % alt_dist)
                    #Check if distance is shorter than it was originally
                    if ( alt_dist < self.graph[alt_y][alt_x] or self.graph[alt_y][alt_x] == -1):
                        self.graph[alt_y][alt_x] = alt_dist
            toSearch[curr_y][curr_x] += 1

#Traversal algorithm
# Set of coordinates that represent the position not yet visited
if __name__ == "__main__":
    graph = Graph(16, 8)
    graph.traverse(0, 7, 5, 5)
    graph.printGraph()
