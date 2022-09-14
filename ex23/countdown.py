import time  # import the time module
import sys ,os

st = time.time()

def countdown(t): # define the countdown func.
    
    while t:
        mins , secs = divmod(t, 60) # The divmod() function returns a tuple containing the quotient

        timer = '{:02d}:{:02d}'.format(mins, secs)

        print(timer, end='\r')
        time.sleep(1)
        t -= 1

    print("Timeout")

t = input("Enter time in Seconds: ")  # input time in seconds

countdown(int(t)) # function call

et = time.time()

elapsed_time = et -st
time.sleep(0.5)
print(f"Start Time:{time.ctime(st)} \nEnd Time:{time.ctime(et)}")

time.sleep(0.5)
print('Execution time:', elapsed_time, 'Seconds')