# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

# Task 1 - printing single object

print('_________________TASK1_______________')

i = int(92)
flo = float(92.27)
com = complex (6+3j)
st = str("Hello")
boo = bool(True)

print(i , flo , com , st , boo, sep='\n')

# Task 2 - printing type of given value

print('_________________TASK2_______________')

print( i,type(i) ,sep=' is type of ')
print( flo,type(flo) ,sep=' is type of ')
print( com,type(com) ,sep=' is type of ')
print( st,type(st) ,sep=' is type of ')
print( boo,type(boo) ,sep=' is type of ')

# Task 3 - checking type of value

print('_________________TASK3_______________')

print(isinstance(i , int))
print(isinstance(flo , bool))
print(isinstance(com , complex))
print(isinstance(st , str))
print(isinstance(boo , float))

#Task 4 - checking type of value (version 2)

print('_________________TASK4_______________')

print('Is', i ,'an instance of Type (int)?',isinstance(i , int))
print('Is',flo, 'an instance of Type (bool)?' , isinstance(flo , bool))
print('Is',com, 'an instance of Type (complex)?' ,isinstance(com , complex))
print('Is',st, 'an instance of Type (string)?' ,isinstance(st , str))
print('Is',boo, 'an instance of Type (float)?' ,isinstance(boo , float))

#Task 5 - using comments in code

print('_________________TASK5_______________')

"""
This function  is to take the user input and to check if the statements are  correct if not the user will get a massage with the instruction.
"""
def generate_strong_password():
    
    length = int(input('Enter password Length: ')) 

    if length < 8: # To check if the giving Value meet the minimum required 

        print('A strong password should be at least 8 Characters! ')
        length = int(input('\nEnter password Length again: '))

    alphabets_count = int(input('Enter alphabets count: '))
    digits_count = int(input('Enter digits count: '))
    special_characters_count = int(input('Enter special characters count: '))

    characters_count = alphabets_count + digits_count + special_characters_count

    # check if characters count is greater then password length
    if characters_count > length:
        print('Characters count can not be greater then the password length.')
        return(generate_strong_password())