#class to do.....
class Rectangle:
  def __init__(self, length, width):
    self.length= length
    self.width= width
  def area(self):
    return (self.length*self.width)
  def perimeter(self):
    return 2*(self.length + self.width)
R=Rectangle(4,4)
print(R.area())
print(R.perimeter())