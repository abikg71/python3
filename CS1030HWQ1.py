'''
Abinet Kenore
CS1030 HW#6 
Due for July 27, 2018
Instruction
Write a Python program named SalesTransaction.
This program should ask the user to enter the price
and name of purchased item. The program should then
compute the state and county sales tax. Assume the state sales tax
is 4 percent and the county sales tax is 2 percent.
The program should display the item name, price of the item,
the state sales tax, the county sales tax, the total sales tax,
and the total of the sale (which is the sum of the amount of
purchase plus the total sales tax).
Hint: Use the value 0.02 to represent 2 percent, and 0.04 to represent 4 percent.
'''

def main():
    #Display program header
    print("Well Come to this Store")
    print("-----------------------------")
    print("How many Items did you purchase")
    choose = 0
    while choose != 3:
        print("Choose from the Options below")
        print("1. One item only \n" "2. More than One item \n"
              "3. To Exit the system \n")
        choose = int(input())
        if choose != 0:
            if choose == 1:
                sales_one_transaction()
            elif choose == 2:
                sales_more_transactions()
            elif choose ==3:
                print("You exit the System")
        else:
            print("The program will now exit\m"
                  "Have Good Day")

print("The program will now exit!")
def sales_one_transaction():

    print()
    print("Okay you purcchased only one item")
    items = str(input("Enter the purchased Item name"))
    price = float(input("Enter the price of purchased Item"))

    tol_price = price
    state_tax = 0.04  * price   # states sales tax
    county_tax = 0.02  * price  #county sales tax
    tol_tax = 0.06 *price

    print("-" *50)
    print("-" *50)
    print("the item name ",items + "\nprice of the item ", price,
      "\n the state sales tax " ,state_tax, "\n the county sales tax"
       ,county_tax, "\nthe total sales tax " , tol_tax,
      "\nthe total of the sales price is  " , tol_price)
    print()

def sales_more_transactions():
    #This def will need improvement and design change
    print()
    items_list = str(input("enter the list of items you bought" .split(",")))
    print("You have purchased: " ,items_list)
    pricess = input(("Please entner Student score list separated by ,"))
    pricess= [int(x) for x in pricess.split(',')]
    sum = 0
    for number in pricess:
        sum += number
        state_tax = 0.04  * sum   # states sales tax
        county_tax = 0.02  * sum  #county sales tax
        tol_tax = 0.06 * sum
    print("Total Amt paid is: ", sum)
    print("the state sales tax " ,state_tax)
    print("the county sales tax " ,county_tax)
    print("the total sales tax " , tol_tax)
    print("the total of the sales price is  " , sum)
    print()

main()
