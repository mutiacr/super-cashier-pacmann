#Import required libraries
import os
from tabulate import tabulate

class Transaction:
    #Create Transaction class which contains several methods needed based on feature requirements
    def __init__(self):
    #Initialize dictionary
        self.items=dict()
  
    def add_item(self, name, quantity, price):
        """
        This method is intended for users to add shopping transaction items which
        consisting of item names, number of items, and price per item.
        """
        self.items[name] = {"name": name, "quantity": quantity, "price": price}
        
    def update_item_name(self, name, new_name):
       """
        This method is intended for users to update name of item 
        that has been previously inputted. 
        """ 
       #Check the name of item
       item = self.items.get(name)
       if item is not None:
          item["name"] = new_name
          #Define new_name as the key
          self.items[new_name] = item
          #Remove old name using .pop
          self.items.pop(name)
          return True
       else:
         raise ValueError("Item not found in the Shopping Cart")
       
    def update_item_quantity(self, name, new_quantity):
        """
        This method is intended for users to update quantity of item 
        that has been previously inputted. 
        """   
        item = self.items.get(name)
        if item:
            item["quantity"] = new_quantity
        else:
            raise ValueError("Item not found in the Shopping Cart")

    def update_item_price(self, name, new_price):
        """
        This method is intended for users to update price of item 
        that has been previously inputted. 
        """ 
        item = self.items.get(name)
        if item:
             item["price"] = new_price
        else:
             raise ValueError("Item not found in the Shopping Cart")

    def delete_item(self, name):
        """
         This method is intended for users to delete the desired item in the transaction list. 
         This method accepts 1 parameter, which is the name of the item to be deleted
         """ 
        if name in self.items:
            del self.items[name]
        else:
            raise ValueError("Item not found in the Shopping Cart")

    def show_items(self):
        """ This method is intended for users to display a transaction input summary"""
        if self.items:
            items = []
            headers = ["Name", "Quantity", "Price","Total Price"]
            for item in self.items.values():
                items.append([item["name"], item["quantity"], item["price"], item["price"]*item["quantity"]])
            print(tabulate(items, headers, tablefmt="fancy_grid"))
            

    def calculate_total(self):
        """This method is intended for users to calculate the total price 
           and discount if the conditions are met"""

        self.show_items()
        #Total calculation formula
        total = sum(i["quantity"] * i["price"] for i in self.items.values())
        
        #Discount calculations using branching conditions
        if total > 500000:
            discount = total * 0.10
            total -= discount
            print("\nSummary:")
            print(f"The total amount is: {total}. You have received a discount of {discount} (10%).")
        elif total > 300000:
            discount = total * 0.08
            total -= discount
            print("\nSummary:")
            print(f"The total amount is: {total}. You have received a discount of {discount} (8%).")
        elif total > 200000:
            discount = total * 0.05
            total -= discount
            print("\nSummary:")
            print(f"The total amount is: {total}. You have received a discount of {discount} (5%).")
        else:
            print("\nSummary:")
            print(f"The total amount is: {total}.")

    def reset(self):
        """This method is intended for users to reset all transaction data"""
        self.items.clear()

    def check_order(self):
        """This method is intended for users to check data input errors in transactions. 
        This method will display text indicating whether 
        the input order is valid or not and lists the items in the transaction in tabular form"""
    
        if self.items!=None:
            print("Order Input is Valid")
        elif  self.items==None:
            print("Order is Invalid")
        print(self.show_items())
   