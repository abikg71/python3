
#Write a Python program that will count the number of vowels in the given string.
#Ref: https://www.geeksforgeeks.org/python-count-display-vowels-string/
#Abinet Kenore

def count_vowels():
    string = str(input("Please enter string"))
    count = 0
        # Creating a set of vowels
    vowel = set("aeiouAEIOU")
    for alphabet in string:
        # If alphabet is present in set vowel
        if alphabet in vowel:
            count = count + 1

    print("Numbers of vowels is :", count)

count_vowels()
