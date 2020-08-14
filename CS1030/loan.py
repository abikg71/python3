'''
The objective of this code is to demonstrate for loop, while loop and conditional statemets
P is the principal amount borrowed
A is the periodic amortization payment
r is the periodic interest rate divided by 100 (nominal annual interest rate also divided by 12 in case of monthly installments), and
n is the total number of payments (for a 30-year loan with monthly payments n

A = p*((r(r + 1)^n)/(((r+1)^n)-1))
'''

# r = 5.8
# P = 10000
# n = 60
# monthly_payemet = 180
# I = P * r

# A = P*((r*(r + 1)**n)/(((r+1)**n)-1))
# for a in range(n):
#     print("Amount is " + "{:.2f}".format(A))

# new_bal = P - (monthly_payemet - (r/(n*100)))
# if new_bal != 0:
#
#     #new_bal = P - (monthly_payemet - (r/(n*100)))
#     print(new_bal)
#     print(A)


# P = int(input("Enter starting principle please: "))
# n = int(input("Enter number of compounding periods per year: "))
# r = float(input("Enter annual interest rate: "))
# y = int(input("Enter the amount of years: "))
# FV = P * (((1 + ((r/100.0)/n)) ** (n*y)))
# print ("The final amount after", y, "years is", FV)
