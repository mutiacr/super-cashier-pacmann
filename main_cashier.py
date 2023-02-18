from transaction_cashier import Transaction
import os
t = Transaction()

#Import random letters and numbers to create Transaction ID 
import random
import string

'''get random Transaction_ID length 8 with letters and numbers'''
characters = string.ascii_letters + string.digits 
Transaction_ID = ''.join(random.choice(characters) for i in range(10))


#Method for Transactions's Main Menu
def main():
    while True:
        os.system('clear')
        print(f"=====WELCOME TO SUPER CASHIER=====\n=Your Transation ID:{Transaction_ID}=")
        print("1. Add Item")
        print("2. Update Item Name")
        print("3. Update Item Quantity")
        print("4. Update Item Price")
        print("5. Delete Item")
        print("6. Show Items")
        print("7. Check Order")
        print("8. Calculate Total")
        print("9. Reset")
        print("10. Quit")
        choice = int(input("Enter your choice: "))
  
        if choice == 1:
            name = str(input("Enter item name: "))
            while True:
                try:
                    quantity = int(input("Enter quantity: "))
                    break
                except ValueError:
                    print("Invalid input. Quantity must be an integer. Please try again.")
            while True:
                try:
                    price = int(input("Enter price: "))
                    break
                except ValueError:
                    print("Invalid input. Price must be an integer. Please try again.")
            t.add_item(name, quantity, price)
        elif choice == 2:
            name = (input("Enter item name to update: "))
            new_name = (input("Enter new item name: "))
            if t.update_item_name(name, new_name):
               print(f"You have successfully updated item {name} to {new_name}.")
        elif choice == 3:
            name = (input("Enter item name to update: "))
            new_quantity = int(input("Enter new quantity: "))
            if t.update_item_quantity(name, new_quantity):
               print(f"You have successfully updated item {name}'s quantity to {new_quantity}.")
            else:
               print(f"Item with name {name} was not found in the inventory.")
        elif choice == 4:
            name = (input("Enter item name to update: "))
            new_price = int(input("Enter new price: "))
            if t.update_item_price(name, new_price):
               print(f"You have successfully updated item {name}'s price to {new_price}.")
            else:
                print(f"Item with name {name} was not found in the inventory.")
        elif choice == 5:
            name = input("Enter item name to delete: ")
            t.delete_item(name)
        elif choice == 6:
            t.show_items()   
            input("Press Enter to continue...")
        elif choice == 7:
             t.check_order()
        elif choice == 8:
            t.calculate_total()
            input("Press Enter to continue...")
        elif choice == 9:
            t.reset()
        elif choice == 10:
            break
    print("==Thank you for using Super Cashier!==")

if __name__ == "__main__":
    main()

