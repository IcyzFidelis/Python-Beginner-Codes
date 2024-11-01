# Create an empty list in advance.
shopping_list = []

# Create a function for adding items.
def item():
  new_item = input("What do you want to buy? ")
  shopping_list.append(new_item)
  print(shopping_list)

# A loop for running the "add_item()" function five times.
for i in range(5):
  item()
    
