import argparse
import time
speed = float(0.5)
time.sleep(speed)

parser = argparse.ArgumentParser(description='Enter Firstname , Lastname and Age')
parser.add_argument('-f' , help=' Firstname ')
parser.add_argument('-l' , help=' Lastname ')
parser.add_argument('-a' ,type=int, help=' Age ')
parser.add_argument('--fast' , help=' enable fast mode')

args = parser.parse_args()

if args.fast == None:
    print("Slow mode is active\n")
elif args.fast == "f":
    speed = float(0)
    print("Fast mode activated\n")

if args.f == None:
    args.f = "Hanson"

if args.l == None:
    args.l = "Larry"
    
if args.a == None:
    args.a = "100"

time.sleep(speed)
print(f"Hello {args.f.capitalize()} {args.l.capitalize()}!")

time.sleep(speed)
print(f"\nI see that you have had {args.a} birthdays.")