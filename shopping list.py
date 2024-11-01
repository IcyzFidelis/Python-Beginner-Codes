shopping_list = []

def item():
    new_item = input("What do you want to buy? ")
    shopping_list.append(new_item)

def list():
    for item in shopping_list:
        print(item)

for _ in range(5):
    item()
    list()
