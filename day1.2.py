TOTAL = 0
Dictionary = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9, "ten" : 10 }
Word_number_list = ["one" , "two", "three", "four", "five", "six", "seven", "eight", "nine",]
Numerical_number_lists = ["1" , "2", "3", "4", "5", "6", "7", "8", "9"]
new_digit = 0
txtfile = open("inputday1.txt", "r")
lines = (txtfile.readlines())




for amountoflines in range(len(lines)):#(0-999)
    Textline = (lines[amountoflines])
    for part in Word_number_list:
        if part in Textline:
            wordposition = Textline.find(part)
            #print(f"Word '{part}' found at position {wordposition} in line {amountoflines}: {Textline}")
    for part in Numerical_number_lists:
        if part in Textline:
            numericalpositions = Textline.find(part)
            #print(f"Word '{part}' found at position {wordposition} in line {amountoflines}: {Textline}")
    if wordposition < numericalpositions:
        res = ''.join([i for i in Textline if not i.isdigit()])
        print(res)
    elif numericalpositions < wordposition:
        rex = ''.join([i for i in Textline if i.isdigit()])
        newnumericalnum = rex[0]+ rex[-1]
        TOTAL += int(newnumericalnum)
print(TOTAL)