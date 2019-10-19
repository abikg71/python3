'''
Abinet Kenore
CS 1030 Summer 2018
Write a Python program named BMI. The body mass index (BMI) is often
used to determine whether a person with a sedentary
 lifestyle is overweight or under- weight for his or her height. A person’s
 BMI is calculated with the following formula:
BMI = (Weight * 703) / (Height2)
where weight is measured in pounds and height is measured in inches.
The program should ask the user for their weigh and height, calculate and
 display their BMI, and display a message indicating whether the person has
 optimal weight, is underweight, or is overweight. A sedentary person’s weight
 is considered optimal if his or her BMI is between 18.5 and 25. If the BMI is
  less than 18.5, the person is considered underweight. If the BMI value is
  greater than 25, the person is considered overweight.
'''

def BMI():
    wt = float(input("Please enter your weight in Pounds "))
    # 1ft = 12
    ht = float(input("Please enter your height in inches "))

    bmi = round((wt * 703)/(ht * ht),2) # two decimal place
    if 18.5  <= bmi <= 25:
        print("Your average BMI is: " , bmi, " and you are OPtimal")

    elif bmi  <= 18.5:
        print("Your average BMI is: ", bmi, " and you are Uderweight")

    else:
        print("Your average BMI is: ", bmi, " and you are Overweight")

BMI()



