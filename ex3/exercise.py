# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn


# Basic control flow
'''
In this exercise, we will focus on the usage of the basic control flow operations,       including:  
 - if-else statements,
 - for and while loops, 
 - input from the user,
 - comparison operators,
 - assignment operators,
 - logical operators.
'''

# Task 1 - basic math operations

'''Your task is to write a program which asks the user three times for a number. If number is even print ‘Even number’, else print ‘Odd number’.
'''
print('>>>>> Task1 <<<<<')

count = 0

while count < 3:
    num = int(input('Please Enter Number:\n'))
    if num % 2 == 0:
        print('This Number is Even!\n ')
    else:
        print('This Number is Odd!\n ')

    count = count + 1

# Method2
'''for i in range(3):
    num = int(input('Please Enter Number :'))
    if num %2 == 0:
        print('This Number is Even! ')
    else:
        print('This Number is Odd! ')
'''

#  Task 2 - printing numbers with `range()` function
'''
Your task is to write a program which asks the user about number of arguments in `range()` function.  
If number is 1 program asks for another number and then prints digits from `range()` function with given number.  
If number is 2 program asks for two numbers and then prints digits from `range()` function with given range.  
If number is 3 program asks for three numbers and then prints digits from `range()` function with given range and given step.
'''
print('>>>>>> Task2 <<<<<<')

arg_num = int(input('Enter number of arguments in range(): '))

if arg_num == 3:
    start = int(input('Please Enter start point: '))
    end = int(input('Please Enter end point: '))
    step = int(input('Please Enter the steps to be skipped : '))

elif arg_num == 2:
    start = int(input('Please Enter start point: '))
    end = int(input('Please Enter end point: '))

else:
    arg_num == 1
    start = int(input('Please Enter start point: '))

for i in range(start, end, step):
    if start == 0:
        i += 1
        print(i, end='\n')

# Task 3 - finding divisors of a number

'''
Your task is to write a program which prints all the divisors of a number. 
The number comes from the user's input.

'''
print('>>>>>> Task3 <<<<<<')

num = int(input('Enter Number here: '))

for i in range(1, num + 1):
    if num % i == 0:
        print(i)

# Task 4 - check prime number
'''
Your task is to write a program to check if input number is a prime number.  
>Hint: Prime number divides without rest only by 1 and itself!
'''
print('>>>>>> Task4 <<<<<<')

num = int(input('Check if prime number:'))

if num > 1:
    for i in range(2, num // 2):
        if (num % i) == 0:
            print(num, ' is not prime number')
            break
    else:
        print(num, ' is a prime number')
else:
    print(num, ' is neither prime nor composite')


# Task 5 - FizzBuzz
'''
Your task is to write a program that prints the numbers from 1 to 100.  
 But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.   
 For numbers which are multiples of both three and five print “FizzBuzz”.

'''
print('>>>>>> Task5 <<<<<<')

num = range(1, 101)
for i in num:
    if i % 3 + i % 5 == 0:
        print('FizzBuzz')

    if (i % 3) == 0:
        print('fizz')

    if (i % 5) == 0:
        print('Buzz')

    print(i)

# Task 6 - divisible numbers
'''
Your task is to write a program to print all the numbers between 1000 and 2000 which are divisible by 7 but are not a multiple of 5.
'''
print('>>>>>> Task6 <<<<<<')

for i in range(1000, 2001):
    if (i % 5) == 0:
        continue
    if (i % 7) == 0:
        print(i)
