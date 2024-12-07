# Challenge #3 POO

### I´m Alejandro Bello Leon from "Fenomenoides" team, i attach our logo: 

<details><summary>Get ready to see the great logo: </summary><p>
<div align='center'>
<figure> <img src="https://i.postimg.cc/NFbwf57S/logo-def.png" alt="Defensa Civil" width="400" height="auto"/></br>
<figcaption><b> "we are programmers, not designers" </b></figcaption></figure>
</div>
</p></details><br>

Below is the solution proposed to the challenge:

#### 1. Excercise proposed in class

```python
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
```

#### 2. Restaurant scenario

```python
class MenuItem:
  def __init__(self, name: str, price: float):
    self.name = name
    self.price = price
 
class Beverage(MenuItem):
  def __init__(self, name, price, size: str):
    super().__init__(name, price)
    self.size = size

class Appetizer(MenuItem):
  def __init__(self, name, price, is_vegetarian: bool = False):
    super().__init__(name, price)
    self.is_vegetarian = is_vegetarian

class MainCourse(MenuItem):
  def __init__(self, name, price, protein: str, is_vegetarian: bool = False):
    super().__init__(name, price)
    self.protein = protein
    self.is_vegetarian = is_vegetarian

class Dessert(MenuItem):
  def __init__(self, name, price, topping: str):
    super().__init__(name, price)
    self.topping = topping

class Order:
  def __init__(self):
    self.items = []

  def add_item(self, item: MenuItem) -> None:
    self.items.append(item)

  def calculate_total(self, your_birthday: bool=False) -> str:
    print("Your order is:")
    total = 0
    for item in self.items:
      print(f"{item.name}: ${item.price}")
      total += item.price
    
    print(f"Price: ${total}")

    if your_birthday == True:
      bdiscount = 0.05

    if total > 120000:
      discount = 0.2
    elif total > 90000:
      discount = 0.1
    else:
      discount = 0
    return f"Total: ${total - (total * (discount + bdiscount))}"

class Menu:
  def __init__(self):
    self.menu_items = [
      Appetizer("Nuggets", 12000),
      Appetizer("Onion soup", 14000, True),
      Beverage("Coke", 3000, "Medium"),
      Beverage("Water", 2000, "Medium"),
      Beverage("Coffee", 3500, "Medium"),
      MainCourse("Burger", 20000, "Cow meat"),
      MainCourse("Vurger", 23000, "Bean meat", True),
      MainCourse("Caesar salad", 18000, "Chicken"),
      Dessert("Oreo McFlurry", 13000, "Oreo"),
      Dessert("m&m McFlurry", 13000, "m&m")]

  def show_menu(self) -> None:
    print("\tMenu")
    for item in self.menu_items:
      print(f"{item.name}: ${item.price}")
    print("-------------------------")

  def get_item(self, name: str) -> "MenuItem":
    for item in self.menu_items:
      if name == item.name:
        return item 

if __name__ == "__main__":

  menu = Menu()
  menu.show_menu()
  order = Order()
  order.add_item(menu.get_item("Coke"))
  order.add_item(menu.get_item("Vurger"))
  order.add_item(menu.get_item("Oreo McFlurry"))
  order.add_item(menu.get_item("m&m McFlurry"))
  order.add_item(menu.get_item("Water"))
  order.add_item(menu.get_item("Coffee"))
  order.add_item(menu.get_item("Burger"))
  order.add_item(menu.get_item("Nuggets"))
  order.add_item(menu.get_item("Onion soup"))
  order.add_item(menu.get_item("Caesar salad"))

  print(order.calculate_total(True))

```

