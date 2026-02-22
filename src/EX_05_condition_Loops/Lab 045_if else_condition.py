#probelem to find the max between two

# Logic Building formula

# user input _ two integers
#o/p INt 1 which ever is greater max number will return
# 31.4 or 45.34

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

if num1 > 0 and num2>0:
    print("Number should be positive")
if num1 > num2:
    print("maximum", num1)
else:
    print("minimum", num2)
