# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

# comparison operators
'''
Your task is to write a program which asks the user three times about two integer numbers to compare. 
>Hint: Use `while` loop to perform the same operation more than once!
'''

print('\n>>>>>>Task1<<<<<<\n')
x = 0

while (x < 3):
    num1= int(input('Please Enter first number: '))
    num2= int(input('Please Enter second number: '))

    if num1 != num2:
        print('\nNum1 is not equal to Num2!\n')
    else:
        print('\nNum1 is equal to Num2!\n')

    if num1 >= num2:
        print('\nNum1 is greater than or equal to Num2!\n')
    else:
        print('\nNum1 is not greater than or equal to Num2!\n')

    if num1 < num2 :
        print('\nNum1 is less than Num2!\n')
    else:
        print('\nNum1 is not less than Num2!\n')

    big_nums = None

    if (num1 >= 500) and (num2 >= 500):
        print('\nBoth numbers are big!\n')
        big_nums = True
        print('\nbig_numbers is set to ',big_nums,'\n')
    else:
        print('\nOne number or both are not big!\n')
        big_nums = False
        print('\nbig_numbers is set to ',big_nums,'\n')

        x += 1

# Task 2 - convertion month name to a number of days

print('\n>>>>>>Task2<<<<<<\n')

def day_of_month():
    print('\nList of months: January, February, March, April, May, June, July, August, September, October, November, December')

    month_name = input('\nEnter the name of Month:')
    month_name = month_name.capitalize()

    if month_name == 'February':
       print(month_name,'Number of days: 28/29 days')

    elif month_name in ("April", "June", "September", "November"):
        print('Number of days: 30 days')

    elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
        print('Number of days: 31 days')

    else:
        print('\nWrong month name:',month_name,)
        print('Please try again!!!')
        return(day_of_month())

day_of_month()