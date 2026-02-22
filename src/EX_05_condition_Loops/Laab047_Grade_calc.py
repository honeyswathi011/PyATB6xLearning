 # for a given numerical score(eg.a, b , c, d ,or F)
 # based on the following grading scale
 # A:90-100
 # B:80-89
 # C:70-79
 # D:60-69
 # F: 0-59

 #  logic building Formula

# 1--> user input - score ---. int
# 2. ---> o/p --> str--> A,B

score = int (input ("Enter Score:").strip())

if score >=100 or score <=1:
    print ("you are a superman!! u can't get a grade!!")
else:
    if score >= 90 and score <= 100:
        print("Your grade is A")
    elif score >= 80 and score <= 90:
        print("your grade is B")
    elif score >= 70 and score <= 80:
        print("your grade is C")
    elif score >= 60 and score <= 70:
        print("your grade is D")
    else:
        print("Your grade is F")
