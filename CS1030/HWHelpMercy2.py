def menu ():
    #Display program header
    #print("Student Test Score Entry Program")
    print("-----------------------------")
    choose_menu = ""
    while choose_menu != "n":
        print('Choose an option:')
        print("a - Add item to cart  \n" "r - Remove item from cart\n"
              "c - change item quantity \n""i - Output items' descriptions\n"
              "o - Output shopping cart \n" "q - Quit")
        print("Enter Selection: ")
        choose_menu = str(input())
        print("Enter selection:")
        if choose_menu != "n":
            if choose_menu == "a":
                add_item_to_cart()
            elif choose_menu == "r":
                remove_item_from_cart()
            elif choose_menu == "c":
                change_item_quantity()
            elif choose_menu == "i":
                output_items_description()
            elif choose_menu == "o":
                output_shopping_cart()
            elif choose_menu == "o":
                output_shopping_cart()
            else:
                print("Quit")
        else:
            print("The program will now exit")

print("The program will now exit!")
def add_item_to_cart():
    new_item = str(input("Enter the item: "))
    item_descr = str(input("Enter item description: "))
    item_price = float(input("Entner the item price:"))
    item_quantity = int(input("entner the item quantity:"))
    #Adding a new file to the Existing file
    with open("Shopping_cart.txt", 'a') as file:
        print("Purchase Day\n" , file=file)
        print(new_item, "", item_descr, item_price, item_quantity, file=file)
    print("New item has been added to file !")

def remove_item_from_cart():
    remove_item = str(input("Enter the name of item to remove: "))

def change_item_quantity():
    item_name = str(input("Enter the item name: "))
    new_quantity  = int(input("Enter the new quantity: "))

def output_items_description():
    item_desc = str(input())

def output_shopping_cart():
    output_shopping = str(input("Display"))
    print()

def ItemToPurchase():
    item = 2
    total_cost =0
    for i in range(0, item):
        item_name =  str(input("Entner the item name:"))
        item_price = float(input("Entner the item price:"))
        item_quantity = int(input("entner the item quantity:"))
        cost = item_price * item_quantity
        total_cost+= cost
        print(item_name,int(item_quantity),"@", int(item_price), " = ", cost)
    print("\nTOTAL COST  ", total_cost)
#ItemToPurchase()
def Item_description():
    item_desc = str(input("Enter Item Description"))
def customer():
    custumer_name = str(input("Enter customer name"))
    from datetime import date #2018-04-07
    current_date = date.today()
    print(current_date)
def purchase_date():
    from datetime import date #2018-04-07
    purchase_day = date.today()
    print(purchase_day)

menu()

#Build the item to purchase class with the following specifications
#Attributes
#Item name (string)
# Itemm_price float
#iem_quantity Int
# default constuctor
#Intialo=ize item name = none, item-price = 0, item-quantity = 0
#Method
#print Iem-price c:ost
