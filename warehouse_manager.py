import sys
import csv

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
    print('-----------------------------------------------------------')
    print('-----------------------------------------------------------')
    return

def add_items():
    new_item = input("Name ?: ")
    value_0 = input("Quantity ?: ")
    value_1 = input("Unit ?: ")
    value_2 = input("Unit price ?: ")
    if new_item in items.keys():
        value_0 = float(items[new_item][0]) + float(value_0)    
    items[new_item] = [value_0, value_1, value_2]
    get_items()

def sell_items():
    product = input("What product do you want to sell ?: ")            
    product_quantity = input("How much ?: ")

    if product in items.keys():
        new_quantity = float(items[product][0]) - float(product_quantity)
        items[product][0] = float(new_quantity)
        get_items()
            
    elif product not in items.keys():
        print("I do not have such a product.")
    
    if product not in sold_items.keys():
        sold_items[product] = [product_quantity, items[product][1], items[product][2]]
    
    else:
        sold_items[product] = [float(sold_items[product][0]) + float(product_quantity), sold_items[product][1], sold_items[product][2]]
    
    print('-----------------------------------------------------------')
    print('-----------------------------------------------------------')
    print("Sold items: ")  
    print("Name\tQuantity\tUnit\tUnit Price (PLN)")
    
    for key, value in sold_items.items():
        print(key, '\t', value[0], '\t' * 2, value[1], '\t', value[2])
    print('-----------------------------------------------------------')
    print('-----------------------------------------------------------')
    return

def get_cost():
    cost = [float(value[0]) * float(value[2]) for key, value in items.items()]
    print("All items cost is: ", sum(cost))
    return

def get_income():
    income = [float(value[0]) * float(value[2]) for key, value in sold_items.items()]
    print("Income is: ", sum(income))
    return

def show_revenue():
    cost = [float(value[0]) * float(value[2]) for key, value in items.items()]
    income = [float(value[0]) * float(value[2]) for key, value in sold_items.items()]
    revenue = sum(income) - sum(cost)
    print("Costs: ", sum(cost))
    print("Income: ", sum(income))
    print('-----------------------------------------------------------')
    print("Revenue:", round(revenue, 2))
    return

def save_items():
    with open(r"c:\users\szmis\onedrive\pulpit\kodilla\python\zadania\warehouse\warehouse_items.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Product', 'Quantity', 'Unit', 'Unit Price'])
        for key, value in items.items():
            row = [key] + value
            writer.writerow(row)
    print("Datas saved.")

def save_sales():
    with open(r"c:\users\szmis\onedrive\pulpit\kodilla\python\zadania\warehouse\sales_items.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Product', 'Quantity', 'Unit', 'Unit Price'])
        for key, value in sold_items.items():
            row = [key] + value
            writer.writerow(row) 
    print("Sales saved.")

def load():
    items.clear()
    with open(r"c:\users\szmis\onedrive\pulpit\kodilla\python\zadania\warehouse\warehouse_items.csv", newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            key = row[0]
            value1, value2, value3 = row[1:]
            items[key] = [float(value1), value2, float(value3)]
    print(items)
    
    sold_items.clear()
    with open(r"c:\users\szmis\onedrive\pulpit\kodilla\python\zadania\warehouse\sales_items.csv", newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            key = row[0]
            value1, value2, value3 = row[1:]
            sold_items[key] = [float(value1), value2, float(value3)]
    print(sold_items)
    
    return

def end():
    print('Bye !')
    sys.exit()

while True:
    menu = input("What would you do ?: \n1 - Show \n2 - Add \n3 - Sell \n4 - Costs \n5 - Income \n6 - Revenue \n7 - Save \n8 - Load \n9 - Exit \n")
    if menu not in ['Show', 'Add', 'Sell', 'Costs', 'Income', 'Revenue', 'Save', 'Load', 'Exit']:
        print("Please choose another option.")
        continue
    
    elif menu == 'Show':
        get_items()

    elif menu == 'Add':
        add_items()
    
    elif menu == 'Sell':
        sell_items()
    
    elif menu == 'Costs':
        get_cost()

    elif menu == 'Income':
        get_income()

    elif menu == 'Revenue':
        show_revenue()

    elif menu == 'Save':
        save_items()
        save_sales()

    elif menu == 'Load':
        load()

    elif menu == 'Exit':
        end()