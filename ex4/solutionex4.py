# Task 1 - comparison and logical operators

print("\n---TASK 1--- \n")
n = 0
while (n < 3):
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    if number1 == number2:
        print("Numbers are equal")
    else:
        print("Numbers are not equal")

    if number1 > number2:
        print("First number is greater than second number")
    else:
        print("Second number is greater than first number")

    if number1 >= number2:
        print("First number is greater than or equal to second number")
    else:
        print("Second number is greater than or equal to first number")        
    
    big_numbers = None
    if (number1 > 1000) and (number2 > 1000):
        print("Both numbers are big!")
        big_numbers = True
    else:
        print("Both numbers are not big!")
        big_numbers = False
    print("big_numbers is set to ", big_numbers)
    print("\n")
    n = n + 1


# Task 2 - convertion month name to a number of days

print("\n---TASK 2--- \n")

print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
month_name = input("Input the name of Month: ")

if month_name == "February":
	print("Number of days: 28 or 29 days")
elif month_name in ("April", "June", "September", "November"):
	print("Number of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
	print("Number of days: 31 days")
else:
	print("Wrong month name!") 