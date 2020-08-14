'''
Abinet Kenore
CS 1030, summuer 2016

'''

def full_name():
    first_name = str(input("Please enter you First name"))
    last_name = str(input("Please enter youLast name"))

    print(("-"* 45))
    print("Your full name is: " , first_name.title(), last_name.title())
    print("your initials are: " ,((first_name[0:1]) + "." + (last_name[0:1])).upper())
    print("Length of full name is: ", len(first_name + last_name))

full_name()
