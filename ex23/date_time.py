import datetime
from datetime import datetime as dt  # Import datetime Library
import os

os.system("clear")

print("##################################\n\
#              TASK1             #\n\
##################################\n")
current_datetime = datetime.date.today() # Store Current datetime.

# Print Current Year.
print("The current year is:",current_datetime.year)

#####################################################


print("##################################\n\
#              TASK2             #\n\
##################################\n")

some_date = datetime.date.today()

print("The Current Weekday is:",some_date.weekday())

####################################################


print("##################################\n\
#              TASK3             #\n\
##################################\n")


def Checkleap(Year):

    if Year % 400 == 0 or Year % 100 != 0 and Year % 4 == 0:
        print(f"{Year} is a leap Year!")
    else:
        print(f"{Year} is not a leap Year!")
    
Checkleap(Year=1992)


print("##################################\n\
#              TASK4             #\n\
##################################\n")

date_as_string = "Feb 14 2021 8:30AM"

datetime_object = dt.strptime(date_as_string,'%b %d %Y %I:%M%p')

print(datetime_object)


