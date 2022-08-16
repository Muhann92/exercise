# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

from math import pi
import random

# Conditional statements
'''
In this exercise, we will once more focus on the usage of the conditional statements, including:  
 - if-else statements,
 - input from the user,
 - for and while loops, 
 - comparison operators,
 - assignment operators,
 - logical operators.
'''
# Task 1 - calculate sum

print('\n>>>>>> Task1 <<<<<<')

num1 = int(input('\nEnter first Number: '))
num2 = int(input('Enter second Number: '))
num3 = int(input('Enter third Number: '))

sum  = num1 + num2 + num3

print('\nFirst number: ',num1)
print('Second number: ',num2)
print('Third number: ',num3)

if num1 and num2 == num3:
    print('The triple sum is: ',sum * 3)
else:
    print('The sum is: ',sum)

# Task 2 - get the difference

'''
Your task is to write a Python program to get the difference between a two given numbers (prompted by user).  
If the first number is greater than second then calculate double difference between numbers.  
Otherwise calculate the **absolute** difference between numbers.  
Print out an appropriate message to the user.

'''

print('\n>>>>>> Task2 <<<<<<')

num1  = int(input('Enter First Number: '))
num2 = int(input('Enter Second Number: '))

if num1 > num2:
    result = 2 * (num1 - num2)
else:
    result = abs (num1 - num2)

print(result)

# Task 3 - odd or even number

'''
Your task is to write a Python program to find whether a given number (prompted from the user) is even or odd.  Print out an appropriate message to the user.
'''

print('\n>>>>>> Task3 <<<<<<\n')

num = int(input('Enter number to check: '))

if num % 2 == 0:
    print(num,'is an even number!')
else:
    print(num,'is an odd number!')

# Task 4 - circle area

'''
Your task is to write a Python program which accepts (prompts) the **float** radius of a circle from the user and compute its [area](https://www.mathsisfun.com/geometry/circle-area.html).  
Round the result to two decimals!  
Print out an appropriate message to the user.

'''

print('\n>>>>>> Task4 <<<<<<\n')

radius = float(input('Enter the Radius of a Circle: '))
area   = round(pi * radius ** 2,2)
diameter = radius * 2
circumference = round(2 * pi * radius,2)

print('The area of the circle with radius ',radius,'is:',area)
print('The Diameter of the circle with radius',radius,'is:',diameter)
print('The circumference of the circle with radius',radius,'is:',circumference)


# Task 5 - guess a number
'''
Your task is to write a Python program to guess a number between 1 to 9.

>Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
'''
print('\n>>>>>> Task5 <<<<<<\n')

numlist = []
for i in range(1,11):
        numlist.append(i)

random.shuffle(numlist)

def guess_a_number():
    guess = int(input('Guess a number between 1 and 10: '))
    while True:
        for i in range(1):
            i = random.choice(numlist)
        if guess == i:
            print('Well guessed!')
            break
        else:
            print('Wrong Number, Try Again!')
        return(guess_a_number())
guess_a_number()

# Task 6 - Celsius to Fahrenheit conversion
