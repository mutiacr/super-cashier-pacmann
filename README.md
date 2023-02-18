# Pacmann Python Project: Super Cashier Self-Service


### A. Project Background
&nbsp;&nbsp;Super Cashier is a business process improvement solution for one of Indonesia's major supermarkets, namely by implementing a cashier system that makes it easier for customers to make transactions at supermarkets in a self-service manner. In the future, customers can directly choose and update what items will be purchased at this Supermarket wherever the customer is


### B. Requirements / Objectives
&nbsp;1. Create Features for Super Cashier's Customer Journey service based on these following details:
<ul>
<li>Create a Transaction ID</li>
<li>Inputting shopping items ( Item Name, Number of Items, Price per Item)</li>
<li>Update shopping items without deleting the previous item</li>
<li>Cancel a shopping item purchase (Delete One of the Transaction Items or Reset the Entire Transaction)</li>
<li>Checking the shopping item list and confirming the suitability of the shopping list item </li>
<li>Displays the total spend payable including the discount calculation (If the total spend falls under the discount criteria)</li>
</ul>
&nbsp;2. Create a self-service cashier system using Python programming language<br>
&nbsp;3. Implement function, branching, and data structure materials<br>
&nbsp;4. Implementing the concept of OOP in a designed program<br>
&nbsp;5. Applying clean code based on PEP8


### C. Flowchart
![Super Cashier-1](https://user-images.githubusercontent.com/124477076/217675272-4fee7326-502f-45a7-bf91-0e859e59ccfe.png)

### D. Functions & Attributes
1. `add_item`             : Method that is intended for users to add shopping transaction items which consisting of item names, number of items, and price per item.
2. `update_item_name`     : Method that is intended for users to update name of item that has been inputted
3. `update_item_quantity` : Method that is intended for users to update quantity of item that has been inputted
4. `update_item_price`    : Method that is intended  for users to update price of item that has been inputted
5. `delete_item`          : Method that is  intended for users to delete the desired item in the transaction list. This method accepts 1 parameter, which is the name                             of the item to be deleted
6. `show_items`           : Method that is intended for users to display a transaction input summary 
7. `calculate_total`      : Method that is intended for users to calculate the total price and discount if the conditions are met
8. `reset`                : Method that is intended for users to reset all transaction data
9. `check_order`          : Method that is intended for users to check data input errors in transactions. This method will display text indicating whether the input                             order is valid or not and lists the items in the transaction in tabular form   

### E. Conclusions
1. Super cashier is a service solution that give an ease for supermarket customers to make shopping transactions
2. With the programming features that have been proposed at this time, it is hoped that in the future it will be possible to develop programs related to features, especially in the method of selecting shopping transaction items
