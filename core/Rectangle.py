class Rectangle():
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        self.area = length * breadth
        self.perimeter = 2 * (length + breadth)

#r1 = Rectangle(10, 20)
#print(r1.length, r1.breadth, r1.area, r1.perimeter)

""" Notice self.area and self.perimeter are instance variables, which are derived from other 
instance variables length and breadth and used for computation of area and perimeter of rectangle."""
