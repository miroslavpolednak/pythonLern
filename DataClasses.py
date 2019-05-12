# example of clasess than have only data without logic
# this class you can compare via equal == and will be same
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
