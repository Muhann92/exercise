#STORY PROGRAM
from   colorama             import *
from   art                  import *

# Title
print(Fore.LIGHTRED_EX+"")
tprint("Escaping the Prison", font="tarty1")
print(""+Style.RESET_ALL)
print("\n>>>>> You're in a Prison and you must escape! <<<<<\n")


# Intro
print("\nYour Journey Start Here Or it Ends. ~_~\n")

print("It looks like someone sent you a Package form outside the Prison!?\n"
      ,"\nGuards: Prisoner someone have sent you a Birthday Cake.\n"
      ,"\nFirst Guard: Mate did you Checked the Prisoner Package before?\n"
      ,"\nSecond Guard: Ahm yeah yeah sure i think i did.\n")
print("OKAY THEY LEFT!!!\n")

loop = 0

while True:
      # First Game Event
      while loop == 0:

            # Player Tools_List
            tools = ["(1)File","(2)Teleporter","(3)Rocket Launcher","(4)Drill"]
            if loop == 0:
                  print("Now Take the Cake apart you'll find a set of Tools i have sent you to escape,"
                  ,"Use them Wisely! XD\n")
                  print(" - ".join(tools))
                  choice = input("Pickup a Tool: ")

            # Tool 1 
            if choice == "1":
                  print("\nYou cut out the Prison Cell Window and jumped out.\n")
                  print("Oops:) your Cell is in the 14th floor you'en smashed to the ground and died!\n")
                  print(Fore.LIGHTRED_EX+"")
                  tprint("FAIL", font="tarty1")
                  print(""+Style.RESET_ALL)

                  # Optional Exit Loop
                  exit_game = input("\nDo you want to continue? Y/N:")
                  if exit_game == ("n"):
                        exit()
                  if exit_game == ("y"):
                        loop = 0

            # Tool 2  
            elif choice =="2":
                  print("\nYou’en Teleported into the Shooting ring during trainings hour!(~_~)")
                  print(Fore.LIGHTRED_EX+"")
                  tprint("FAIL", font="tarty1")
                  print(""+Style.RESET_ALL)

                  # Optional Exit Loop
                  exit_game = input("\nDo you want to continue? Y/N:")
                  if exit_game == ("n"):
                        exit()
                  if exit_game == ("y"):
                        loop = 0

            # Tool 3
            elif choice =="3":
                  print("\nRoom is too small you died by the explosion(*-*)")
                  print(Fore.LIGHTRED_EX+"")
                  tprint("FAIL", font="tarty1")
                  print(""+Style.RESET_ALL)

                  # Optional Exit Loop
                  exit_game = input("\nDo you want to continue? Y/N:")
                  if exit_game == ("n"):
                        exit()
                  if exit_game == ("y"):
                        loop = 0

            # Tool 4 and last GAME EVENT
            elif choice =="4":
                  print("\nYou landed into a Room below your Cell,",
                  "it seems to be for collecting Dirty clothes,quit somebody is here\n",
                  "\nGourd: You’er Service worker Right?",
                  "Service_Worker:Yes Mr Officer,we’er about to collect this last Floor,\n",
                  "the container_truck waiting at the end of the Slid.\n")
                  print("\naha here its the Slid to the Container get in quick!")
                  print("\nGreat in few Minutes you’ll be Free...")
                  loop = 1
      else:
            loop == 1
            break


print(Fore.LIGHTRED_EX+"")
tprint("\nYou escaped", font="tarty1")
print(""+Style.RESET_ALL)