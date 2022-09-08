import sys
import time

print("\nName of Python script:",sys.argv[0])
time.sleep(0.5)

arg_len = len(sys.argv)
print("Total arguments passed",arg_len)
time.sleep(0.5)

for i in range(1,arg_len):
    if sys.argv[i] == "--help":
        print("options:\
             \n--help    shows Help message and will exit\
             \n--fast    to activate Fast Mode\
             \nslow mode is by default!")
        break
time.sleep(0.5)

for i in range(1,arg_len):
    if sys.argv[i] == "--fast":
        time.sleep(0)
        print("\n(fast mode enabled)")
    else:
        print("\n(slow mode enabled)")
        break
    