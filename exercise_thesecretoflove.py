# To help them we will write a cipher for their secrets.

# There will be inputs :  the secret ,love name, year of birth.

# Secret condition : The secret must be at least 8 characters.

# The cipher algorithm is :
# 1-Concatenate the love secret with the love name 
# 2-Reverse the string 
# 3-Concatenate the revered string with the year of birth 
# NOTE: We need to cipher the secret itself , not to create a new ciphered string.

# We need there inputs Methods Secret , love Name , year of birth

secret = input(('Please write your Secret here: '))

while True:
    if len(secret) < 8:
        print('\nThe secret must be at least 8 characters.')
        secret = input(('\nPlease write your Secret again: '))
    else :
        len(secret) >= 8
        break

name = input(('\nPlease Enter Your Love Name Here: '))        
y_o_birth = input(('\nPlease Enter The Year Of Birth Here: '))

print( name [::-1]  +secret [::-1]+ y_o_birth)