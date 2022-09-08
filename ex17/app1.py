import sys
import time

speed = float(0.5)
time.sleep(speed)
if "--fast"in sys.argv[1:]:
    speed = 0
    print("Fast mode enabled!")
else:
    print("Slow mode enabled")

time.sleep(speed)
print("\nName of Python script:",sys.argv[0])

time.sleep(speed)
print(f"\nEntered Arguments: {' - '.join(sys.argv[1:])}\n")

time.sleep(speed)
arg_len = len(sys.argv)
print("Total arguments passed",arg_len)

time.sleep(speed)
if  "--help" in sys.argv[1:]:
    print("\noptions:\n\n--help    shows Help message and will exit")
    print("\n--fast    to activate Fast Mode")
    print("\nslow mode is by default enabled!")


    


    