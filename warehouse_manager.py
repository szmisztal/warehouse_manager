import sys

items = {
    'Milk': [120, 'l', 2.3],
    'Sugar': [1000, 'kg', 3],
    'Flour': [12000, 'kg', 1.2],
    'Coffee': [25, 'kg', 40]
}

def get_items():
    print("Name\tQuantity\tUnit\tUnit Price (PLN)")
    print('-----------------------------------------------------------')
    print([key for key in items.keys()][0],'\t', [value for value in items.values()][0][0], '\t' * 2, [value for value in items.values()][0][1], '\t', [value for value in items.values()][0][2])
    print([key for key in items.keys()][1], '\t', [value for value in items.values()][1][0], '\t' *2, [value for value in items.values()][1][1], '\t', [value for value in items.values()][1][2])
    print([key for key in items.keys()][2], '\t', [value for value in items.values()][2][0], '\t' * 2, [value for value in items.values()][2][1], '\t', [value for value in items.values()][2][2])
    print([key for key in items.keys()][3], '\t', [value for value in items.values()][3][0], '\t' *2, [value for value in items.values()][3][1], '\t', [value for value in items.values()][3][2])
    return

def add_items():
    new_item = input("Name ?: ")
    value_0 = input("Quantity ?: ")
    value_1 = input("Unit ?: ")
    value_2 = input("Unit price ?: ")

    items.setdefault(new_item, []).append(value_0)
    items[new_item].append(value_1)
    items[new_item].append(value_2)
    get_items()
    print(new_item, '\t', value_0, '\t' * 2, value_1, '\t', value_2)
    return

def sell_items():
    product = input("Which product want to sell ?: ")
    for key in items.keys():
        if key == product:
            product_quantity = float(input("How many ?: "))
            new_quantity = items[product][0] - product_quantity
            items[product][0] = new_quantity
            get_items()
    
        elif product not in items.keys():
            print("We dont have this product.")
            break
      

def end():
    return print("Bye !"), exit()

while True:
    menu = input("What would you do ?: \n1 - Show \n2 - Add \n3 -Sell \n4 - Exit \n")
    if menu not in ['Show', 'Add', 'Sell', 'Exit']:
        print("Please choose another option.")
        continue
    
    elif menu == 'Show':
        get_items()

    elif menu == 'Add':
        add_items()
    
    elif menu == 'Sell':
        sell_items()
        
    elif menu == 'Exit':
        end()

