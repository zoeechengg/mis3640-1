class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        """return a Point object in human-readable format."""
        return f"({self.x}, {self.y})."

    # we overload a special method
    def __add__(self, other):
        new_point = Point(self.x + other.x, self.y+other.y)
        return new_point

    def __sub__(self, other):
        new_point = Point(self.x - 2* other.x, self.y- 2* other.y)
        return new_point

    def __eq__(self, other):
        return self.x == other.x

    def __len__(self):
        return 100

alvie = Point(3, 4)
# print(alvie.x)
# print(alvie.y)

print(alvie)

andrew = Point(3, 1)
# print(andrew.x, andrew.y)
print(andrew)

aa = alvie + andrew
print(aa) 

p2 = alvie - andrew
print(p2)

print(alvie == andrew)

print(len(alvie))

