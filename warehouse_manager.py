import sys

def end():
    return print("Bye !"), exit()

while True:
    menu = input("What would you do ?: \n 1 - Exit \n").lower()
    if menu not in ('Exit').lower():
        print("Please choose another option.")
        continue
    elif menu == 'exit' and 'Exit':
        end()

