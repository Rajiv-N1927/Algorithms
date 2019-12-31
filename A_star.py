'''
The graph is defined by a 2D array.

Author: Rajiv Narayan

'''
from array import *
import math

# The lowest number that represents a valid coordinate
MIN = 0
# The largest X coordinate
MAX_X = 0
# The largest Y coordinate
MAX_Y = 0
# Boundary
BOUNDARY = '|'
# Infnite value
INF = -1
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

    def heuristic(pos, dest):
        return

    #traverse a path diven the starting and ending position in the graph
    def traverse(self, x_start, y_start, x_end, y_end):
        if (not self.withinBounds(x_start, y_start)):
            raise ArithmeticError("Entered start coordinates exceeds map limits")
        if (not self.withinBounds(x_end, y_end)):
            raise ArithmeticError("Entered end coordinates exceeds map limits")
