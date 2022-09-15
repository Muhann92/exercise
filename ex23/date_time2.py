from datetime import datetime , timedelta
import os


os.system("clear")

print("##################################\n\
#              TASK1             #\n\
##################################\n")

current_datetime = datetime.now()
sub_delta = timedelta(days= 15)
cu_day = current_datetime - sub_delta
# reformat datetime to string
date_time_str = datetime.strftime(cu_day,'%Y-%m-%d')
print(date_time_str)

#################################################

print("##################################\n\
#              TASK2             #\n\
##################################\n")

add_delta = timedelta(days= 7)

c_day = current_datetime + add_delta

re_day = datetime.strftime(c_day,'%Y-%m-%d')

print(re_day)

################################################

print("##################################\n\
#              TASK3             #\n\
##################################\n")

# Reminder message to customer.
reminder = "Hello Friedrich, your rent of 300 € is due on 25 January, 2021." 

# Creating a datetime 
start_date = datetime(year=2022, month=9, day=25)





