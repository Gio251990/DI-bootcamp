# Coffee Shop Menu Manager

# Initial data
menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}

def show_menu(menu_dict):
    if len(menu_dict) == 0:
        print("The menu is empty.")
    else:
        print("Current menu:")
    for keys, values in menu.items():
            print(f"{keys} - {values}₪")

def add_item(menu_dict):
    drink = input("Enter new drink name: ")
    if drink in menu_dict:
        print("Item already exists!")
    else:
        price = input("Enter price: ")
        menu_dict[drink] = float(price)
        print(f"{drink} added")


def update_price(menu_dict):
    drink = input("Which drink do you want to update? ")
    if drink in menu_dict:
        new_price = input("Enter the new price: ")
        menu_dict[drink] = float(new_price)
        print("Price updated!")
    else:
        print("Item not found.")
    print()


def delete_item(menu_dict):
    drink = input("Which drink do you want to delete? ")
    if drink in menu_dict:
        del menu_dict[drink]
        print("Item deleted!")
    else:
        print("Item not found.")
    print()


def show_options():
    print("What would you like to do?")
    print("1 Show menu")
    print("2 Add item")
    print("3 Update price")
    print("4 Delete item")
    print("5 Exit")


def run_coffee_shop():
    while True:
        show_options()
        choice = input("> ")
        if choice == "1":
            show_menu(menu)
        elif choice == "2":
            add_item(menu)
        elif choice == "3":
            update_price(menu)
        elif choice == "4":
            delete_item(menu)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
            print()

run_coffee_shop()
