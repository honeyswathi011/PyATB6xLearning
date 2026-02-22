# find the  positive number is even or odd
num = int(input("Enter a number: ").strip())

if num > 0:
    if num % 2 == 0:
        print("Even")
    else :
        print("Odd ")
else:
    print("Negative number")

# you can write in single oneliner conditions using the ternary operator

if num > 0:
    print("Even" if num % 2 == 0 else "odd")
else:
    print("Negative number")