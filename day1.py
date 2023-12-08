TOTAL = 0
txtfile = open("inputday1.txt", "r")
lines = (txtfile.readlines())

for i in lines:
    s = ''.join(x for x in i if x.isdigit())
    First_digit = s[0]
    Second_digit = s[-1]
    new_digit = int(First_digit + Second_digit)
    TOTAL += new_digit
print(TOTAL)


#Take the amount of lines 
#Go read through each line 
#Find the first integer and multiple it by 10 
#Find second integer and multiple it by 1 or not 
#Add them both together
#Add them to a variable