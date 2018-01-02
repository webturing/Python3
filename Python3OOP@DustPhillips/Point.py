import math


class Point:
    """
    init method
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    """
    reset
    """
    def reset(self):
        self.x = 0
        self.y = 0
    '''
    other doc
    '''
    def distance(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)


p = Point()
print(p.x, p.y)
p.reset()
print(p.x, p.y)
q = Point(3, 4)
print(p.distance(q))
