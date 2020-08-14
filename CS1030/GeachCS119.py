'''
Nov 24, 2018
This project is about the shopping. In this project I will write about 
the shopping which I do every week
'''


def ShoppingItems():
     items = ['orange', 'oil', 'soap', 'floor', 'milk', 'chips', 'banana']
     price = [6.88, 17.15, 5, 24, 2.45, 1.322, 9 ]
     print("Well Come to the G_Grocery Store!\n")
     result = zip() # No iterabes are passed
     resultList = list(result) # Converting itertor to list
     result = zip(items, price) # Two iterables are passed
     resultSet = set(result) # Converting itertor to set
     print(resultSet)
     print()
    
     total_cost = 0
     i, p =  zip(*resultSet)
     print('c =', i)
     print('v =', p)
     shopped_item =  str(input("Entner the item you shopped: "))
     while(shopped_item  is not None ):
         shopped_item =  str(input("Entner the item you shopped: "))
         price_of_item = float(input("Entner the item price:"))
         item_quantity = int(input("entner the item quantity:"))
         
         if(shopped_item not in items):
             print(shopped_item in items, " Not Found!")
             break
         cost = price_of_item * item_quantity
         total_cost+= cost
     print(int(item_quantity),shopped_item,"@", int(price_of_item), " = ", cost)
     print("========================\nTOTAL COST  ", total_cost)

def main():
    ShoppingItems()
main()