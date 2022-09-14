import time

'''
EXERCISE:
Create a program that
- saves current time and prints it
- saves another time moment and prints it
- prints the time that has passed in between
'''

ct = time.ctime()
et = time.time()
pt = ct - et
print(pt)