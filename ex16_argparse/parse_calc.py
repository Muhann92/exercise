import argparse

parser = argparse.ArgumentParser(description="Basic Calculator")

parser.add_argument('num1', type=int,help="input first number")
parser.add_argument('op',help="input operant")
parser.add_argument('num2',type=int, help="input second number")

args = parser.parse_args()

if args.op == "+":
    result = args.num1 + args.num2
elif args.op == "-":
    result = args.num1 - args.num2
elif args.op == "x":
    result = args.num1 * args.num2
elif args.op == "/":
    result = args.num1 / args.num2


print(str(args.num1) + args.op + str(args.num2) + "=" + str(result))