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
    print('Milk','\t', items['Milk'][0], '\t' * 2, items['Milk'][1], '\t', items['Milk'][2])
    print('Sugar', '\t', items['Sugar'][0], '\t' *2, items['Sugar'][1], '\t', items['Sugar'][2])
    print('Flour', '\t', items['Flour'][0], '\t' * 2, items['Flour'][1], '\t', items['Flour'][2])
    print('Coffee', '\t', items['Coffee'][0], '\t' *2, items['Coffee'][1], '\t', items['Coffee'][2])
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

def end():
    return print("Bye !"), exit()

while True:
    menu = input("What would you do ?: \n1 - Show \n2 - Add \n3 - Exit \n")
    if menu not in ['Show', 'Add', 'Exit']:
        print("Please choose another option.")
        continue
    
    elif menu == 'Show':
        get_items()

    elif menu == 'Add':
        add_items()
    
    elif menu == 'Exit':
        end()

