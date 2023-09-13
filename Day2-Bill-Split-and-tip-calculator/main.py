#100DaysofPython - Day 2 Project  - Bill Split and Tip Calculator

#Introduction
print("Welcome to the Bill Split and Tip Calculator")

#Total Cost
total = input("Please input the total bill cost: ")

#Split Cost
split = input("Please input how many people will split the bill: ")

#Tip Percentage
tip = input("Please input the tip percentage you would like to give: (Input the number without the percentage) ")

#refactoring
float_total = float(total)
float_split = float(split)
float_tip = float(tip)

#result
total_result = float(float_tip / 100 * float_total + float_total)
split_result = float(total_result / float_split)
rounded_result = round(split_result, 2)
rounded_result = "{:.2f}".format(rounded_result)

print(f"Cost that should be split is: $ {rounded_result}")