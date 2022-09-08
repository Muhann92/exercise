# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn
import math

'''
Your task is to check in action every basic math operators with combination of integers, floating point numbers, complex numbers and booleans. Do at least two calculations for every operator. 
Also make use of [round()](https://www.w3schools.com/python/ref_func_round.asp) function to round your floating point results to specific number of decimals.  
You can mix integer with floats inside given math operation.  
> Hint: You can assign math operation to a variable, and then perform another math operation on this variable
'''

# Task 1 - basic math operations

print('---------->Task1<----------')

add       = 27 + 12
add2      = 19 + 92

subtract  = 1992 - 2022
subtract2 = 80 - 29

multiply  = 7 * 3
multiply2 = 9 * 6

divide    = 365 / 12
divide2   = 120 / 6

modulo    = 13 % 4
modulo2   = 16 % 2

power     = 6 ** 8 
power2    = 8 ** 6 

floor     = 9.3567
floor2    = 2.7181

boo       = True + False
boo2      = True * False

comp      = 6 * (3 - 1j)
comp2     = 12 * (4 - 6j)

print('\n>>>>> ADD <<<<<')
print(str('27 + 12 ='),add)
print(str('19 + 92 ='),add2)

print('\n>>>>> SUBTRACT <<<<<')
print(str('1992 - 2022 ='),subtract)
print(str('80 - 29 ='),subtract2)

print('\n>>>>> MULTIPLY <<<<<')
print(str('7 * 3 ='),multiply)
print(str('9 * 6 ='),multiply2)

print('\n>>>>> DIVIDE <<<<<')
print(str('365 / 12 ='),divide)
print(str('120 / 6 ='),divide2)

print('\n>>>>> MODULO <<<<<')
print(str('13 % 4 ='),modulo)
print(str('16 % 2 ='),modulo2)

print('\n>>>>> POWER <<<<<')
print(str('6 ** 8 ='), power)
print(str('8 ** 6 ='), power2)

print('\n>>>>> FLOOR ROUNDING <<<<<')
print(str('9.3567 // 2 ='), round(floor , 2))
print(str('2.7181 ='), round(floor2))

print('\n>>>>> BOOLEANS <<<<<')
print(str('True + False ='),boo)
print(str('True * False ='),boo2)

print('\n>>>>> COMPLEX <<<<<')
print(str('6 * (3 - 1j) ='),comp)
print(str('12 * (4 - 6j) ='),comp2)

# comment
print('---------->Task2<----------')

# Task 2 - basic math functions

'''Your task is to check in action every basic math function mentioned earlier with combination of integers, floating point numbers, complex numbers and booleans. Do at least two calculations for every function.
'''
# max() Math function(maximum value)
print(str('max(31 , 19, -52)'), max(31 , 19, -52),sep='= ')
print(str('max(9.5 ,4.2, -12)'), max(9.5 ,4.2, -12),sep='= ')

# min() Math function(minimum value)
print(str('min(11 , 2 , 0.80)'), min(11 , 2 , 0.80),sep='= ')
print(str('min(7.1 , 3.6 , 1.25)'), min(0.11 ,1.9, 1.25),sep= '= ')

# abs() Math function(absolute value)
print(str('abs(-71.71)'), abs(-71.71),sep='= ')
print(str('abs(-12.95+round(-55,2)'),abs(-12.95+round(-55,2)),sep='= ')

# pow() Math function(value to the power of the value)
print(str('pow(12.5,3)'),pow(12.5,3), sep='= ')
print(str('pow(2.5,7)+ round(18,2)'),pow(2.5,7)+round(18,2),sep='= ')

# ceil() Math function(rounds a number upwards to its nearest integer)
print(str('math.ceil(45/8)'),math.ceil(45/9),sep='= ')
print(str('math.ceil(36.60 /7)'),math.ceil(36.60 / 7),sep='= ')

# floor() Math function(rounds a number downwards to its nearest integer)
print(str('math.floor(63/11)'),math.floor(63/7),sep='= ')
print(str('math.floor(105.91/7)'),math.floor(105.91 / 7),sep='= ')

# max() Math function(maximum value)
print(str('True , False'),max(True , False),sep=' = ')
print(str('False , True'),max(False , True),sep=' = ')

# abs() Math function(absolute value)
print(str('abs(5 - 6j)'),abs(5.3 - 6j),sep='= ')
print(str('abs(9.1 - 2j)'),abs(9.1 - 2j),sep='= ')



print('\n>>>>>>>>> Task1 & Task2 <<<<<<<<<<')
print('>>>>>>>>>>> Are Done <<<<<<<<<<')