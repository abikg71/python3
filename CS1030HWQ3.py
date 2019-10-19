'''
A software company sells a package that retails for $ 99.
Quantity discounts are given according to the following table:
size     Discount
10 - 19  20%
20 - 49  30%
50 - 99  40%
> = 100  50%
Write a program that asks the user to enter the number of packages
 purchased. The program should then display the amount of the discount
  (if any) and the total amount of the purchase after the discount.
  Use nested if else statement
Abinet Kenore
CS 1030 Summer 2018
'''

def sell_packages():
    pgk_size = int(input("Please enter the package size you purchased "))
    pkg_price = 99
    discount_price = final_payement = 0
    reg_price = pgk_size * pkg_price

    if 10  <= pgk_size <= 19:
        discount_price = 0.02 * reg_price
        final_payement = reg_price - discount_price

    elif 20  <= pgk_size <= 49:
        discount_price = 0.03 * reg_price
        final_payement = reg_price - discount_price

    elif 50  <= pgk_size <= 99:
        discount_price = 0.04 * reg_price
        final_payement = reg_price - discount_price

    elif pgk_size >= 100:
        discount_price = 0.05 * reg_price
        final_payement = reg_price - discount_price

    else:
        print("There is no Discount  and the price is : $", reg_price)
        final_payement = reg_price - discount_price

    print("- " * 50)
    print()
    print("The orginal price of the item before discount is: $",round(reg_price, 4))
    print("The discount you get is: $",round(discount_price, 4))
    print("The price of the item after discount is: $",round(final_payement, 4))

sell_packages()

