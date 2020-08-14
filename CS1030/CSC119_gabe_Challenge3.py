#This program is using defining of the function
def totalExpense(expense):
    total = 0
    for price in expense:
        total = total + price
    return total          
def averageExpense(expense):
    total = 0

     # Declare variables using the loop total expense 
    for price in expense:
        total = total + price
    avg = total / len(expense)
    return avg 

def main():

	#Obtain the calculation
    expense = []
    items = ["officeRent","electric","vehicles","cableTV","telephone","internet","payroll","marketing","production","shipping"]
    print("Company Name: Mountain Steelworks, Inc.\n")
    print("Street Address: 16000 East CenterTech Parkway")
    print("City: Aurora")
    print("State: Co")
    print("State Full: Colorado")
    print("Zipcode: 80011")

    print("Please enter the monthly expenses for the following items: ")

    for item in items:
        temp = int(input(item + ": "))
        expense.append(temp)
        temp = 0
    i = 0

    #Displaying th item names and their expenses using the loop
    print("ITEM NAME\t\t\t\tExpense")
    for item in items:
        print(item + "\t\t\t\t" + str(expense[i]))
        i = i + 1
    
    total = totalExpense(expense)
    avg = averageExpense(expense)
    maximum = max(expense)
    minimum = min(expense)
    print("Total expense is: $%.2f" % total)
    print("Average expense is $%.2f" % avg)
    print("Maximum expense is: $%.2f" % maximum)
    print("Minimum expense is $%.2f" % minimum)

if __name__ == '__main__':
    main()
