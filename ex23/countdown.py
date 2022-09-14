import time  # import the time module
import os

st = time.time() # Capture Start Time

def countdown(t): # define the countdown func.
    
    while t:
        mins , secs = divmod(t, 60) # The divmod() function returns a tuple containing the quotient

        timer = '{:02d}:{:02d}'.format(mins, secs) # Str.format

        print(timer, end='\r')
        time.sleep(0.5)
        t -= 1

    os.system("clear") # clear Terminal

    print("Timeout!!!\n")

t = input("Enter time in Seconds: ")  # input time in seconds

countdown(int(t)) # function call

et = time.time() # Capture End Time

tg =  t # Time given
time.sleep(1)
print("Seconds counted down: ",tg)

elapsed_time = et -st # Calculate taking time to finish

time.sleep(1)
print(f"Start Time: {time.ctime(st)} \nEnd Time: {time.ctime(et)}")

time.sleep(1)
print('Execution time:', round(elapsed_time), 'Seconds')