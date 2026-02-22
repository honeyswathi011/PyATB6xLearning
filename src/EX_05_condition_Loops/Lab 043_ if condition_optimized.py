# write a program to take a user age and
# let him know if he can go to the club or not
from idlelib.debugger_r import close_subprocess_debugger

#  logic Building Formula
# age > 21 -. print can go to club)
# age< 21 -- print can't go
age=int(input("enter the age\n").strip())
if age <=0 or age > 130:
    print("enter a valid age")
else:
    if age >=21:
        print("yes you can go to club")
    else:
        print("No you can't go to club")


 #Step 4 .check for the edge cases
 # we should consider the edge cases such as
# Negative ages and extremely high values - progress will break
# Non numeric Input-ABC
# Age which is valid >130

#  step 5. Optimize the code
#  Handle all the edge