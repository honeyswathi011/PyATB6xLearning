# problem find the max between 3 numbers

#Logic Building

# @user input  -num1 num2 num3 --> int
#o/p---> int or string with max numbers

num1 = int(input("enter the num \n"))  # 5 , 10
num2 = int(input("enter the num2 \n")) # 3 , 12
num3 = int (input("Enter the num3 \n")) # 2, 11
# 5 > 3, 5 > 2---> 5
 #num1 > num 2 and num1 > num 3--> num1
 #num2 > num3 and num2> num1 -->  num 2
 #num3-max
if num1 >= num2 and num1 >= num3:
     print("Max",num1)
elif num2 >= num3 and num2 >=num1:
    print("Max",num2)
else:
    print(num3)

