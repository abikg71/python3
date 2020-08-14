# Define your person class below
class Person():
    def __init__(self, first, last, email):
        self.first_name = first
        self.last_name = last
        self.email_address = email

    def getFullName(self): #class
        return "{} {} {}" .format(self.first_name,self.last_name,self.email_address)

#Define your customer class below
class Customer():
    def __init__(self,first,last,email, customer_number):
        super().__init__(first,last,email,customer_number)
        self.customer_number = customer_number

#Define you employee class below
class Employee(Person):
    def __init__(self,first,last,email, SSN):
        super().__init__(first,last,email,SSN)
        self.social_security_number = SSN

def main():
    #Customer, Employee,customer_number,social_security_number
    print("Customer/Employee Data Entry")
    print("Enter c for customer, e for employee, q to quit")
    choose_menu = ""
    while choose_menu != "q":
        choose_menu = str(input())
        print("Enter selection:")
        if choose_menu != "q":
            if choose_menu == "c":
                Customer()
            elif choose_menu == "e":
                Employee()
        else:
            print("The program will now exit")

#Finish the main function below

    print("Bye!")

def get_input(choice):
    print("DATA ENTRY")
    # Finish this function to retrieve input
    first_name = str(input("Enter first name"))
    last_name = str(input("Enter last name"))
    email_address = str(input("Enter email address name"))
    main()
def display(person):
    print()
# Complete this function using isinstance()
if __name__ == "__main__":
    main()
    employee = Employee()
    customer = Customer()

    employee.getFullName()
    customer.customer_number()