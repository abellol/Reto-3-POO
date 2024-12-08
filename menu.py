
class MenuItem:
  """
  base class that define general parameters for each item from menu

  Attributes:
    name (str): Name of the item from menu
    price (float): Price of the item from menu
  """
  def __init__(self, name: str, price: float):
    """
  Initializes the class with values for name and price.

  Args:
    name (str): The initial value for name.
    price (int): The initial value for price.
    """
    self.name = name
    self.price = price
 
class Beverage(MenuItem):
  """
  A subclass of MenuItem that represent Beverage

  Inherits:
    MenuItem: The base class

  Aditional Atributes:
    Size: The size of the beverage
  """

  def __init__(self, name, price, size: str):
    super().__init__(name, price)
    self.size = size

class Appetizer(MenuItem):
  """
  A subclass of MenuItem that represent Appetizer

  Inherits:
    MenuItem: The base class

  Aditional Atributes:
    is_vegetarian: If the food is vegetarian or not
  """
  
  def __init__(self, name, price, is_vegetarian: bool = False):
    super().__init__(name, price)
    self.is_vegetarian = is_vegetarian

class MainCourse(MenuItem):
  """
  A subclass of MenuItem that represent Beverage

  Inherits:
    MenuItem: The base class

  Aditional Atributes:
    Protein: The protein of the maincourse
    is_vegetarian: If the food is vegetarian or not
  """
  
  def __init__(self, name, price, protein: str, is_vegetarian: bool = False):
    super().__init__(name, price)
    self.protein = protein
    self.is_vegetarian = is_vegetarian

class Dessert(MenuItem):
  """
  A subclass of MenuItem that represent Beverage

  Inherits:
    MenuItem: The base class

  Aditional Atributes:
    Topping: The topping of each dessert
  """

  def __init__(self, name, price, topping: str):
    super().__init__(name, price)
    self.topping = topping

class Order:
  """
  Calculates the total price of the order, applying discounts based on
  the total amount and whether it's the customer's birthday.
  Discounts:
   - Birthday discount: 5% (if `your_birthday` is True).
   - Total over 120,000: 20% discount.
   - Total over 90,000: 10% discount.
   - No discount for totals below 90,000.
  Args:
    your_birthday (bool): Whether it's the customer's birthday. Defaults to False.
  
  Methods:
    add_item(item: MenuItem) -> None:

    calculate_total(your_birthday: bool = False) -> str:
       
  """
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
  """
  Represents a menu containing various menu items, including appetizers, beverages,
  main courses, and desserts.

  Attributes:
    menu_items (list): A list of predefined menu items, each represented as an instance
    of a specific subclass (e.g., Appetizer, Beverage, MainCourse, Dessert).

    Methods:
    show_menu() -> None:
      Displays the menu items with their names and prices.

    get_item(name: str) -> MenuItem:
      Retrieves a menu item by its name.
  """

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
  # Example menu
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
