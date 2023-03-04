import sys

items = {
    'Milk': [120, 'l', 2.3],
    'Sugar': [1000, 'kg', 3],
    'Flour': [12000, 'kg', 1.2],
    'Coffee': [25, 'kg', 40]
}

sold_items = {}

def get_items():
    print("Name\tQuantity\tUnit\tUnit Price (PLN)")
    print('-----------------------------------------------------------')
    for key, value in items.items():
        print(key, '\t', value[0], '\t' * 2, value[1], '\t', value[2])
    return

def add_items():
    new_item = input("Name ?: ")
    value_0 = input("Quantity ?: ")
    value_1 = input("Unit ?: ")
    value_2 = input("Unit price ?: ")
    items[new_item] = [value_0, value_1, value_2]
    get_items()

def sell_items():
    product = input("Which product want to sell ?: ")
    for key in items.keys():
        if key == product:
            product_quantity = float(input("How many ?: "))
            new_quantity = float(items[product][0]) - product_quantity
            items[product][0] = new_quantity
            sold_items[product] = [product_quantity, items[product][1], items[product][2]]
            get_items()
            
        elif product not in items.keys():
            print("We dont have this product.")
            break

def get_cost():
    cost = [value[0] * value[2] for key, value in items.items()]
    print("All items cost is: ", sum(cost))
    return

def end():
    return print("Bye !"), exit()

while True:
    menu = input("What would you do ?: \n1 - Show \n2 - Add \n3 - Sell \n4 - Cost \n5 - Exit \n")
    if menu not in ['Show', 'Add', 'Sell', 'Cost', 'Exit']:
        print("Please choose another option.")
        continue
    
    elif menu == 'Show':
        get_items()

    elif menu == 'Add':
        add_items()
    
    elif menu == 'Sell':
        sell_items()
    
    elif menu == 'Cost':
        get_cost()
        
    elif menu == 'Exit':
        end()

