# Special priority Queue for the A_star algorithm
#
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == []

    def size(self):
        return len(self.queue)
    # for inserting an element in the queue
    # The data comes in a tuple defined as (x_coordinate, y_coordinate, fScore)
    def insert(self, data):
        if ( type(data) in [tuple] and len(data) is 3 ):
            self.queue.append(data)
        else: # For testing
            raise TypeError("The input data must be a size 3 tuple, containing\
            in the form (x_coord, y_coord, fScore)")
    # for popping an element based on fScore Priority
    def pop(self):
        try:
            pos = 0
            (x_min, y_min, fScoreMin) = self.queue[pos]
            for i in range(len(self.queue)):
                (x, y, fScore) = self.queue[i]
                if fScore < fScoreMin:
                    (x_min, y_min, fScoreMin) = self.queue[i]
                    pos = i
            item = (x_min, y_min)
            del self.queue[pos]
            return item
        except IndexError:
            print()
            exit()
