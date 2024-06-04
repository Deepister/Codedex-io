# Write code below 💖
class Restaurant:
  name = ''
  category = ''
  rating = 0.0
  delivery = False

bobs_burgers = Restaurant()
republic = Restaurant()

bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

republic.name = 'Republic'
republic.category = 'Burger Joint'
republic.rating = 3.0
republic.delivery = True

print(vars(bobs_burgers))
print(vars(republic))