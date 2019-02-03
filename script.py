class Menu:
  
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return "{} menu available from {} and {}!".format(self.name, self.start_time, self.end_time)
    
  def calculate_bill(self, purchased_items):
    tot = 0
    for item in purchased_items:
      tot += self.items[item]
    return tot

items1 = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}  

brunch = Menu('brunch', items1, 11, 16)


items2 = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird = Menu('early_bird', items2, 15, 18)

items3 = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner = Menu('dinner', items3, 17, 23)

items4 = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu('kid', items4, 11, 21)

print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))


class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return "The address is {}".format(self.address)
  
  def available_menus(self, time):
    mm = [menu for menu in self.menus if time >= menu.start_time and time <=menu.end_time]
    return mm
  

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
print(flagship_store.available_menus(12))

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_place = Franchise("189 Fitzgerald Avenue", Menu('arepas_menu', arepas_menu, 10, 20))

aa = Business("Take a' Arepa", arepas_place)
print(aa.franchises)

    
    
  