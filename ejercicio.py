import math

class Point:
  def __init__(self, x: float, y: float):
    self.x = x
    self.y = y

class Line:
  def __init__(self, start: Point, end: Point):
    self.start = start
    self.end = end

  def compute_length(self):
    dx = self.start.x - self.end.x
    dy = self.start.y - self.end.y
    return ((dx**2 + dy**2)**0.5)
  
  def compute_slope(self):
    dx = abs(self.start.x - self.end.x)
    dy = abs(self.start.y - self.end.y)
    return(f"The slope of the line with the x axis is {math.degrees(math.atan2(dy, dx))}°")

  def compute_horizontal_cross(self):
    point1 = self.start.y
    point2 = self.end.y
    return(f"Cross with x axis: {point1 * point2 < 0}")  
    
  def compute_vertical_cross(self):
    point1 = self.start.x
    point2 = self.end.x
    return(f"cross with y axis: {point1 * point2 < 0}")
  
  def dicretize_line(self, size):
    points = []
    scalex = 0
    scaley = 0
    dx = (self.end.x - self.start.x) / (size)
    dy = (self.end.y - self.start.y) / (size)
    for i in range(size):
      scalex += dx
      scaley += dy
      points.append((self.end.x - scalex, self.end.y - scaley))

    return points

class Rectangle:
  def __init__(self, width1: Line, height1: Line, width2: Line, height2: Line):
    self.width1 = width1
    self.height1 = height1
    self.width2 = width2
    self.height2 = height2
    
  def compute_area(self):
    return(f"Area: {self.height1.compute_length() * self.width1.compute_length()}")

  def compute_perimeter(self):
    return(f"Perimeter: {self.width1.compute_length() + self.height1.compute_length() + self.width2.compute_length() + self.height2.compute_length()}")


if __name__ == "__main__":

  # First Line
  start1 = Point(0,0)
  end1 = Point(0,5)

  line1 = Line(start1, end1)
  print(line1.compute_length())
  print(line1.compute_slope())
  print(line1.compute_horizontal_cross())
  print(line1.compute_vertical_cross())

  print("-----------------------------------")

  # Second line
  start2 = Point(0,0)
  end2 = Point(4,0)

  line2 = Line(start2, end2)
  print(line2.compute_length())
  print(line2.compute_slope())  
  print(line2.compute_horizontal_cross())
  print(line2.compute_vertical_cross())
  

  print("-----------------------------------")

  # Third line
  start3 = Point(4,0)
  end3 = Point(4,5)

  line3 = Line(start3, end3)
  print(line3.compute_length())
  print(line3.compute_slope())  
  print(line3.compute_horizontal_cross())
  print(line3.compute_vertical_cross())

  print("-----------------------------------")
  
  # fourth line
  start4 = Point(0,5)
  end4 = Point(4,5)

  line4 = Line(start4, end4)
  print(line4.compute_length())
  print(line4.compute_slope())
  print(line4.compute_horizontal_cross())
  print(line4.compute_vertical_cross())

  print("-----------------------------------")

  # rectangle
  rectangle1 = Rectangle(line1, line2, line3, line4)
  print(rectangle1.compute_area())
  print(rectangle1.compute_perimeter())


  # exmaple line dicretize
  start5 = Point(1,2)
  end5 = Point(5,4)
  line5 = Line(start5, end5)
  print(line5.dicretize_line(5))




  
