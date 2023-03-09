import sys
import csv

items = {}
sold_items = {}

if len(sys.argv) > 1:
    filename = sys.argv[1]
    try:
        with open(r"c:\users\szmis\onedrive\pulpit\kodilla\python\zadania\warehouse\warehouse_items.csv", newline='') as file:
            reader = csv.reader(file)
            headers = next(reader)
            for row in reader:
                key = row[0]
                value1, value2, value3 = row[1:]
                items[key] = [float(value1), value2, float(value3)]
        print('File', filename, 'load.')
        print("Remember to load sold items !")
    except FileNotFoundError:
        print("File not found: ", filename)
else:
    filename = input("Filename path: ")
    try:
        with open(r"c:\users\szmis\onedrive\pulpit\kodilla\python\zadania\warehouse\warehouse_items.csv", newline='') as file:
            reader = csv.reader(file)
            headers = next(reader)
            for row in reader:
                key = row[0]
                value1, value2, value3 = row[1:]
                items[key] = [float(value1), value2, float(value3)]
        print('File', filename, 'load.')
        print("Remember to load sold items !")
    except FileNotFoundError:
        print("File not found: ", filename)

def get_items():
    print("Name\tQuantity\tUnit\tUnit Price (PLN)")
    print('-----------------------------------------------------------')
    for key, value in items.items():
        print(key, '\t', value[0], '\t' * 2, value[1], '\t', value[2])
    print('-----------------------------------------------------------')
    print('-----------------------------------------------------------')
    return

def add_items():
    while True:
        try:
            new_item = str(input("Name ?: "))
            value_0 = float(input("Quantity ?: "))
            value_1 = str(input("Unit ?: "))
            value_2 = float(input("Unit price ?: "))
            if new_item in items.keys():
                value_0 = float(items[new_item][0]) + float(value_0)    
            items[new_item] = [value_0, value_1, value_2]
        except ValueError:
            print("Name and unit must be only letters, quantity and unit price must be only numbers.")
            continue
        question = input("Do you want add another item ? 1 - Yes, 2 - No: ")
        if question in ['1', 'yes', 'Yes']:
            continue
        elif question in ['2', 'no', 'No']:
            get_items()
            break
        elif question not in ['1', 'yes', 'Yes', '2', 'no', 'No' ]:
            print("Wrong value, try again.")
            break

def sell_items():
    while True:
        try:
            product = str(input("What product do you want to sell ?: "))            
            product_quantity = float(input("How much ?: "))
            if product in items.keys():
                new_quantity = float(items[product][0]) - float(product_quantity)
                items[product][0] = float(new_quantity)
            elif product not in items.keys():
                print("I do not have such a product.")
    
            if product not in sold_items.keys():
               sold_items[product] = [product_quantity, items[product][1], items[product][2]]
            else:
                sold_items[product] = [float(sold_items[product][0]) + float(product_quantity), sold_items[product][1], sold_items[product][2]]
        except ValueError:
            print("Name product must be only letters, quantity must be only numbers.")
            continue
        question = input("Do you want sell another item ? 1 - Yes, 2 - No: ")
        if question in ['1', 'yes', 'Yes']:
            continue
        elif question in ['2', 'no', 'No']:
            get_items()
            break
        elif question not in ['1', 'yes', 'Yes', '2', 'no', 'No' ]:
            print("Wrong value, try again.")
            break
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
    
    sold_items.clear()
    with open(r"c:\users\szmis\onedrive\pulpit\kodilla\python\zadania\warehouse\sales_items.csv", newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            key = row[0]
            value1, value2, value3 = row[1:]
            sold_items[key] = [float(value1), value2, float(value3)]

    return

def end():
    print('Bye !')
    sys.exit()

while True:
    menu = input("What would you do ?: \n1 - Show \n2 - Add \n3 - Sell \n4 - Costs \n5 - Income \n6 - Revenue \n7 - Save \n8 - Load \n9 - Exit \n")
    if menu not in ['1', 'show', 'Show', '2', 'add', 'Add', '3', 'sell', 'Sell', '4', 'costs', 'Costs', '5', 'income', 'Income', '6', 'revenue', 'Revenue', '7', 'save', 'Save', '8', 'load', 'Load', '9', 'exit', 'Exit']:
        print("Please choose another option.")
        continue
    
    elif menu in ['1', 'show', 'Show']:
        get_items()

    elif menu in ['2', 'add', 'Add']:
        add_items()
    
    elif menu in ['3', 'sell', 'Sell']:
        sell_items()

    elif menu in ['4', 'costs', 'Costs']:
        get_cost()

    elif menu in ['5', 'income', 'Income']:
        get_income()

    elif menu in ['6', 'revenue', 'Revenue']:
        show_revenue()

    elif menu in ['7', 'save', 'Save']:
        save_items()
        save_sales()

    elif menu in ['8', 'load', 'Load']:
        load()

    elif menu in ['9', 'exit', 'Exit']:
        end()