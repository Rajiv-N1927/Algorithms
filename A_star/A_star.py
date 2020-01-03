'''
The graph is defined by a 2D array.

The graph is traversed using a diagonal based approach. That is going
up, down, left or right is considered 1 unit and going diagonal is considered
sqrt(2).

Author: Rajiv Narayan

'''
from array import *
import math
from Priority_Queue import PriorityQueue as PQ

# The lowest number that represents a valid coordinate
MIN = 0
# The largest X coordinate
MAX_X = 0
# The largest Y coordinate
MAX_Y = 0
# Boundary
BOUNDARY = '|'
# Infnite value
INF = math.inf
# A point is surrounded by 8 other elements therefore a point can be searched up
# to 8 times before it has been oversearched. This is not taking into account
# points that are on the corner which are only surrounded by 3 or points on the
# side which are only surrounded by 5
MAX_SEARCH = 8
# No currently defined previous node for shortest path
NO_POS = (-1, -1)
# The initial position
INITIAL_POS = (-2, -2)

class Graph:
    #Define the dimensions of the graph
    def __init__(self, dim_x, dim_y):
        self.cols, self.rows = (dim_x, dim_y)
        global MAX_X, MAX_Y
        MAX_X = dim_x
        MAX_Y = dim_y
        #Defining a 2D array with distances set as -1 (for infinitely long)
        #All adjascent coordinates are length 1 away
        self.graph = [[INF for x in range(self.cols)] for y in range(self.rows)]

    def printGraph(self):
        for item in self.graph:
            print(item)

    def setPointAs(self, x_coord, y_coord, val):
        self.graph[y_coord][x_coord] = val

    def setBoundary(self, coords):
        for coord in coords:
            (x, y) = coord
            self.graph[y][x] = BOUNDARY
    def withinBounds(self, x_coord, y_coord):
        return (x_coord >= MIN and x_coord < MAX_X) \
            and (y_coord >= MIN and y_coord < MAX_Y) and self.graph[y_coord][x_coord] != BOUNDARY

    def heuristic(self, pos, dest):
        return 0

    def path(self, path_arr, start, end):
        pos = (end[0], end[1])
        while ( pos != (start[0], start[1]) ):
            (curr_x, curr_y) = path_arr[pos[1]][pos[0]]
            pos = (curr_x, curr_y)
            self.graph[curr_y][curr_x] = '-'
        self.graph[start[1]][start[0]] = 'x'
        self.graph[end[1]][end[0]]     = 'x'
        self.printGraph()
    #traverse a path diven the starting and ending position in the graph
    def traverse(self, start_pos, end_pos, heuristic):
        (x_start, y_start) = start_pos
        (x_end, y_end) = end_pos
        if (not self.withinBounds(x_start, y_start)):
            raise ArithmeticError("Entered start coordinates exceeds map limits")
        if (not self.withinBounds(x_end, y_end)):
            raise ArithmeticError("Entered end coordinates exceeds map limits")
        self.graph[y_start][x_start] = 0
        #Copying Wikipedia
        openSet = PQ()
        prev = [[NO_POS for x in range(0, MAX_X)] for y in range(0, MAX_Y)]
        #gScore  = [[INF for x in range(self.cols)] for y in range(self.rows)]
        self.graph[y_start][x_start] = 0
        fScore  = [[INF for x in range(self.cols)] for y in range(self.rows)]
        fScore[y_start][x_start] = heuristic(start_pos, end_pos)
        # Checks for the nodes that have already been visited
        toSearch = [[[] for x in range(0, MAX_X)] for y in range(0, MAX_Y)]
        openSet.insert((x_start, y_start, fScore[y_start][x_start]))
        # Go through the algorithm
        while ( openSet.size() > 0 ):
            (curr_x, curr_y) = openSet.pop()
            if ( (curr_x, curr_y) == end_pos ):
                for f in fScore:
                    print(f)
                print("\n\n")
                return self.path(prev, start_pos, end_pos)
            # Check the positions of all the neighbours
            intPos = [[(intx, inty) for intx in range(curr_x-1, curr_x+2)]
                        for inty in range(curr_y-1, curr_y+2)]
            for coord in intPos:
                for pos in coord:
                    (alt_x, alt_y) = pos
                    if (not self.withinBounds(alt_x, alt_y)): continue
                    if ((alt_x, alt_y) in toSearch[curr_y][curr_x]): continue
                    toSearch[alt_y][alt_x].insert(0, (curr_x, curr_y))
                    # Get the distance of the node from the starting position
                    gScore = self.graph[curr_y][curr_x]
                    #Find the distance between the current position and the next
                    t_gScore = gScore + math.sqrt(math.pow(alt_x-curr_x, 2) + math.pow(alt_y-curr_y, 2))
                    t_gScore = float("%.1f" % t_gScore)
                    #Check if distance is shorter than it was originally
                    if ( t_gScore < self.graph[alt_y][alt_x]):
                        self.graph[alt_y][alt_x] = t_gScore
                        prev[alt_y][alt_x] = (curr_x, curr_y)
                        fScore[alt_y][alt_x] = self.graph[alt_y][alt_x]
                        + heuristic((alt_x, alt_y), end_pos)
                        # Add to the current Queue
                        if ( not openSet.contains((alt_x, alt_y)) ):
                            openSet.insert((alt_x, alt_y, fScore[alt_y][alt_x]))

if __name__ == "__main__":
    graph = Graph(8, 8)
    gate = graph.setBoundary([(3, y) for y in range(2, MAX_Y-1)])
    graph.traverse((2, 3), (6, 5), graph.heuristic)
    #graph.printGraph()
